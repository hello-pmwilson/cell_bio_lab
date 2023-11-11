from django.urls import path
from . import views

app_name = 'lab_website'

urlpatterns = [
    path("", views.home, name="home"),
]