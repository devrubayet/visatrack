from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='home'),
    path('track-application/', track_application, name='track_application'), 
    # path('track-visa/', track_visa, name='track_visa'), # URL for AJAX request
    path('visa-details/<str:visa_name>/', visa_details, name='visa_details'),
    path('package-details/<str:package_name>/', package_details, name='package-details'),
    path('contact-us/', contact_us, name='contact-us'),

]
