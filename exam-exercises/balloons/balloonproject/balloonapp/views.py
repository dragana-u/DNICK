from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from balloonapp.forms import FlightForm
from balloonapp.models import Flight


# Create your views here.

def index(request):
    return render(request, 'index.html')

def flights(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
        return redirect('index')
    form = FlightForm()
    flights_inst = Flight.objects.filter(user=request.user)
    return render(request, 'flights.html', context={'form': form, 'flights': flights_inst})
