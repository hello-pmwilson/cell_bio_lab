from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inventory"),
    path("inventory", views.inventoryView, name="inventory"),
    path("requests", views.requests, name="requests"),
    path("add", views.itemAdd, name="item_add"),
]