from django.urls import path

from . import views

app_name = "helper"

urlpatterns = [
    path("", views.index, name="index"),
    path("activities/", views.activities, name="activities"),

]
