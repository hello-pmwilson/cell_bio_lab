from django.shortcuts import render
from .forms import onRequestForm, inventoryAddForm, itemAddForm
from .models import inventory, on_request, item

# Create your views here.
def index(request):
    #check if specific template is called to load, and if not set default
    if 'selected' in request.GET:
        selected = request.GET['selected']
    else:
        selected = 'inventory' #set the default

    #based on selected template, load data to fill in html
    if selected == 'inventory':
        form = inventoryAddForm(request.POST or None)
        ordering = 'inventory'
        q = inventory.objects.all().order_by(ordering)
        defaultURL = 'inventory/inventory.html'
    elif selected == 'requests':
        form = onRequestForm(request.POST or None)
        ordering = 'item'
        q = on_request.objects.all().order_by(ordering)
        defaultURL = 'inventory/requests.html'
    elif selected == 'add_item':
        form = itemAddForm(request.POST or None)
        ordering = 'item'
        q = item.objects.all().order_by(ordering)
        defaultURL = 'inventory/add_item.html'        

    #check if order_by is set and update the query accordingly
    if 'order_by' in request.GET:
        ordering = request.GET['order_by']
        q = inventory.objects.all().order_by(ordering)

    #if form submitted, check validity and save
    if request.method == "POST":
        if form.is_valid():
            form.save()

    #save finalized values and render page
    context = {
        'defaultURL': defaultURL,
        'form': form,
        'data': q
    }
    return render(request, 'inventory/index.html', context)