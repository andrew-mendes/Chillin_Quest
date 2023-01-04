import requests, json

from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import dateparse
from django.views.decorators.csrf import csrf_protect

from .forms import UploadFileForm

from .models import Outbreak


# Reads Google Maps API Key from file
key_file = open("app\maps_api_key.txt", "r")
api_key = key_file.read()
key_file.close()

#### VIEWS ####

# Calculates % change of fires from previous day
def get_difference(request, date):
    previous_date = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)
    current_count = Outbreak.objects.filter(date=date).count()
    previous_count = Outbreak.objects.filter(date=previous_date).count()
    
    if not current_count or not previous_count:
        return JsonResponse({"Dif": ""})
    else:
        try:
            dif = "{:.2f}".format((abs(current_count - previous_count) / previous_count) * 100.0)
        except current_count == previous_count or ZeroDivisionError:
            return JsonResponse({"Dif": 0})

        if previous_count > current_count:
            dif = "-" + dif
        elif previous_count < current_count:
            dif = "+" + dif
        
        return JsonResponse({"Dif": dif})


# retrieves fire outbreaks data from the DB
def get_fires(request, date):
    fires = Outbreak.objects.filter(date=date)
    return JsonResponse([fire.serialize() for fire in fires], safe=False)


# Renders homepage
def index(request):
    try:
        # Defines date range according to available data in the DB
        max_date = Outbreak.objects.latest('date').date
        min_date = Outbreak.objects.earliest('date').date
        max_month = datetime.strftime(max_date,'%Y-%m')
        min_month = datetime.strftime(min_date,'%Y-%m')
    except:
        # Avoids bugs if opening the website without data in the DB
        min_date = max_date = min_month = max_month = ""
    return render(request, "app/index.html", {
        "api_key": api_key,
        "current_time": datetime.now(),
        "max_date": str(max_date),
        "min_date": str(min_date),
        "min_month": min_month,
        "max_month": max_month,
    })


# Filters data in order to build line and bar charts
def build_chart(request, range, start, end):
    # Gathers data for rendering charts of fires per day
    if range == "day":
        # Filters dates and firecounts between the two selected dates
        infos = list(Outbreak.objects.filter(date__gte=start, date__lte=end)\
                .values('date')\
                .annotate(**{'total': Count('date')})
        )
        return JsonResponse(infos, safe=False)

    # Gathers data for rendering charts of fires per month
    elif range == "month":
        monthstart = start[5:]
        monthend = end[5:]
        yearstart = start[:4]
        yearend = end[:4]
        
        # Filters dates and firecounts between the two selected dates
        infos = list(Outbreak.objects.filter(\
            date__month__gte=monthstart, date__month__lte=monthend,\
            date__year__gte=yearstart, date__year__lte=yearend)\
            .annotate(month=TruncMonth('date'))\
            .values('month')\
            .annotate(**{'total': Count('date')})
        )
        return JsonResponse(infos, safe=False)


# Filters data in order to build donut charts
def build_donut(request, date):
    # Slices input date strings chosen parts
    month = date[5:]
    year = date[:4]

    # Filters dates and firecounts between the two selected dates
    infos = list(Outbreak.objects.filter(date__month=month, date__year=year)\
        .values('date')\
        .annotate(**{'total': Count('date')})
    )
    return JsonResponse(infos, safe=False)


# Filters data in order to build the list of fires on a date
def build_list(request, date):
    fires = Outbreak.objects.filter(date=date)
    return JsonResponse([fire.serialize() for fire in fires], safe=False)


@csrf_protect
@staff_member_required(login_url='/admin')
# Collects fire outbreaks data from INPE and saves on the DB
def data_collect(request):
    # OPTION 1: GEOJSON file upload
    # - This option is to be used in case INPE's website is unavailable
    # or in order to populate the DB with data not in the last 24h.
    # - The file can be request the desired period data at the following link:
    # https://queimadas.dgi.inpe.br/queimadas/bdqueimadas#exportar-dados
    # - Make sure to check all inputs correctly in order to filter the data.
    process_start = datetime.now()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Gets data from file input form
                file = request.FILES['file']
                try:
                    data = json.load(file)
                    datetime_name = 'datahora'
                    # Filters wanted data from JSON and saves on the DB
                    for key in data['features']:
                        # Calls sorting function
                        data_sort(key, datetime_name)
                # Catches and display file errors
                except json.JSONDecodeError as e:
                    print(e)
                    error = str(e)
                    messages.error(request, "Error: " + error)
                    return HttpResponseRedirect(reverse("admin:index"))
                # Reports successful operation
                print("Data collect started on ", process_start, " and completed on ", datetime.now())
                messages.success(request, "Database update successful")
                return HttpResponseRedirect(reverse("admin:index"))
            # Catches an reports other errors
            except Exception as e:
                error = str(e)
                form = UploadFileForm()
                print("Error: " + error)
                messages.error(request, "Error: " + error)
                return HttpResponseRedirect(reverse("admin:index"))
    
    # OPTION 2: Connect with INPE's API
    # - Provides data from the last day
    # - Updates everyday around 6pm GMT-3
    else:
        try:
            # Requests data from the API
            response = requests.get('http://queimadas.dgi.inpe.br/api/focos/?pais_id=33')
            try:
                data = json.loads(response.text)
                # Filters wanted data from JSON and saves on the DB
                datetime_name = 'data_hora_gmt'
                for key in data:
                    # Calls sorting function
                    data_sort(key, datetime_name)
            # Catches and reports json errors
            except json.JSONDecodeError as e:
                print(e)
                messages.error(request, "Error: " + error)
            if response:
                # Reports successful operation
                print("Data collect started on ", process_start, " and completed on ", datetime.now())
                messages.success(request, "Database update successful")
                return HttpResponseRedirect(reverse("admin:index"))
        # Catches and reports connection errors
        except Exception as e:
            error = str(e)
            messages.error(request, "Error: " + error)
            print("Error: " + error)
            return HttpResponseRedirect(reverse("admin:index"))


#### FUNCTION ####


# Filters results by data from INPE's reference satellite:
def data_sort(key, datetime_name):
    try:
        if key['properties']['satelite'] == "AQUA_M-T" and key['properties']['pais'] == "Brasil":
            fire = Outbreak()
            fire.satellite = key['properties']['satelite']
            fire.latitude = key['properties']['latitude']
            fire.longitude = key['properties']['longitude']
            # Downloaded GEOJSON files' datetime fields are named "datahora" and separated by "/"
            if datetime_name == 'datahora':
                fire.date = datetime.strptime(key['properties']['datahora'], '%Y/%m/%d %H:%M:%S').date()
            # JSON files from the API's datetime fields are named "data_hora_gmt" and separated by "-"
            else:
                timestamp = dateparse.parse_datetime(key['properties']['data_hora_gmt'])
                fire.date = datetime.strptime(str(timestamp), '%Y-%m-%d %H:%M:%S+00:00').date()
            fire.city = key['properties']['municipio']
            fire.state = key['properties']['estado']
            fire.save()
            print(datetime.now(), "- COLLECTED: ", fire)
    # Reports errors in key/values such as duplication
    except IntegrityError as e:
        print(e)