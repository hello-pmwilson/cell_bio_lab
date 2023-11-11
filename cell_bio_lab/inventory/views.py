from django.shortcuts import render
from .forms import onRequestForm 
from .forms import inventoryAddForm

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

def requests(request):
    context = {}
    form = onRequestForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['requestForm']= form
    return render(request, 'inventory/requests.html', context)

def inventoryAdd(request):
    context = {}
    form = inventoryAddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['addInventoryForm']= form
    return render(request, 'inventory/add_inventory.html', context)

def inventory(request):
    return render(request, 'inventory/inventory.html')
  