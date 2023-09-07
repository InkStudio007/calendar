from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.main_calendar, name='main_calendar'),
    path('', views.current_calendar, name='current_calendar'),
]