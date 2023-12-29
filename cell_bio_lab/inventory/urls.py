from django.urls import path
from . import views

urlpatterns = [
    path("", views.inventoryView, name="inventory"),
    path("requests", views.requests, name="requests"),
    path("add", views.inventoryAdd, name="inventory_add"),
]