from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('air_passenger_rights/', views.air_passenger_rights, name='air_passenger_rights'),
    path('overbooked_flights/', views.overbooked_flight, name='overbooked_flight'),
    path('delayed_flights/', views.delayed_compensation_flights, name='delayed_compensation_flights'),
    path('cancelled_flights/', views.cancel_flight, name='cancel_flight'),
    path('services/', views.services, name='services'),
    path('submit_claim/', views.submit_claim, name='submit_claim'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
]
