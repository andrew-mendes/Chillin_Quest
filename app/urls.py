from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # API Routes
    path("get_fires/<str:date>", views.get_fires, name="get_fires"),
    path("get_difference/<str:date>", views.get_difference, name="get_difference"),
    path("build_chart/<str:range>/<str:start>/<str:end>", views.build_chart, name="build_chart"),
    path("build_donut/<str:date>", views.build_donut, name="build_donut"),
    path("build_list/<str:date>", views.build_list, name="build_list"),
    # Admin data collect
    path("admin/data_collect", views.data_collect, name="data-collect"),
]
