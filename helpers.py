# Load modules
# Flask
from flask import redirect, render_template, session
# Python
import datetime
from functools import wraps

# Establish allowed image input formats
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Verifies upload file allowed extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Renders error messages
def error(message, code):
    
    # Enables paragraph division on messages
    message = message.split("\n")

    return render_template("error.html", message=message, code=code)


# Enables mandatory login for access to pages
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# Converts date to a worldly understood format
def knowdate():

    date = datetime.datetime.now()
    day = date.strftime('%d')
    month = date.strftime('%m')
    year = date.strftime('%Y')
    hour = date.strftime('%H:%M')
    monthname = None

    # Name months
    if month == '1':
        monthname = 'Jan'
    elif month == '2':
        monthname = 'Feb'
    elif month == '3':
        monthname = 'Mar'
    elif month == '4':
        monthname = 'Apr'
    elif month == '5':
        monthname = 'May'
    elif month == '6':
        monthname = 'Jun'
    elif month == '7':
        monthname = 'Jul'    
    elif month == '8':
        monthname = 'Aug'
    elif month == '9':
        monthname = 'Sep'    
    elif month == '10':
        monthname = 'Oct'
    elif month == '11':
        monthname = 'Nov'            
    elif month == '12':
        monthname = 'Dec'
    
    message = 'Completed on {}/{}/{} at {}'.format(day, monthname, year, hour)
    
    return message
