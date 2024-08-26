from django.urls import path
from .views import Calendar

urlpatterns = [
    path('calendar/', Calendar, name='calendar'),
]
