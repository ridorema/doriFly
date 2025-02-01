from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def services(request):
    return render(request, 'website/services.html')

def air_passenger_rights(request):
    return render(request, 'website/air-passenger_rights.html')

def cancel_flight(request):
    return render(request, 'website/cancel_flight.html')

def delayed_compensation_flights(request):
    return render(request, 'website/delayed_compensation_flights.html')

def overbooked_flight(request):
    return render(request, 'website/overbooked_flight.html')

def submit_claim(request):
    return render(request, 'website/submit_claim.html')

def signup(request):
    return render(request, 'account/Signup.html')
def login(request):
    return render(request, 'account/login.html')

