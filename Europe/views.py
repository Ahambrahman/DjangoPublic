from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Trip
# Create your views here.

def index(request):
    context = {
        "trips": Trip.objects.all(), 
        
    }
    return render(request, "trips/index.html", context)

def create_trip(request):
    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        nights = int(request.POST['nights'])
        price = int(request.POST['price'])
        
        Trip.objects.create(origin=origin, destination=destination, nights=nights, price=price)
        return redirect('index')  # Redirect to the trip list view

    return render(request, 'trips/create_trip.html')