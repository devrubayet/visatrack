from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='home'),
    path('track-application/', track_application, name='track_application'),  # URL for AJAX request

]
