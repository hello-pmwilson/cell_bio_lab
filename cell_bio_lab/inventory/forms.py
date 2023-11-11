from django import forms
from .models import on_request
from .models import inventory

class onRequestForm(forms.ModelForm):
    class Meta:
        model = on_request
        fields = "__all__"

class inventoryAddForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = "__all__"