from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_weather, name='weather'),
    path('facebook', views.fb, name='fb'),
    path('instagram', views.ig, name='ig'),
]
