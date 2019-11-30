from django.shortcuts import render
from .models import Driver
from .models import Kid

def retrieve_kids_drivers(request):
    getdrivers = Driver.objects.all()
    getkids = Kid.objects.all()
    return render(request, 'display_data.html', {'drivers':getdrivers, 'kids':getkids})
