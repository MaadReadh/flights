
from django.shortcuts import render

from work.flights.models import Flight

# Create your views here.
def index(request):
  return render(request, 'Flights/index.html')