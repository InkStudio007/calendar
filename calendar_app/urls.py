from django.urls import path
from . import views
from date_division_app.views import *

urlpatterns = [
    path('<int:year>/<str:month>/', views.main_calendar, name='main_calendar'),
    path('', views.current_calendar, name='current_calendar'),
    path('date_difference/', date_difference, name='date_difference')
]