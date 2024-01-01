from django.shortcuts import render
from .forms import onRequestForm, inventoryAddForm
from .models import inventory, on_request

# Create your views here.
def index(request):
    defaultURL = 'inventory' #set default view to be loaded in content
    return render(request, 'inventory/inventory.html', {'defaultURL': defaultURL})

def requests(request):
    context = {}
    form = onRequestForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['requestForm']= form
    context['data'] = on_request.objects.all()
    return render(request, 'inventory/requests.html', context)

def itemAdd(request):
    context = {}
    form = inventoryAddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['addInventoryForm']= form
    return render(request, 'inventory/add_inventory.html', context)

def inventoryView(request):
    context = {}
    context['data'] = inventory.objects.all()
    addInventoryForm = inventoryAddForm(request.POST or None)
    context['addInventoryForm']= addInventoryForm  
    if request.method == "POST":
        if addInventoryForm.is_valid():
            print("bvalis")
            addInventoryForm.save()
    return render(request, 'inventory/inventory.html', context)

def itemAdd(request):
    return render(request, 'inventory/add_item.html')

  