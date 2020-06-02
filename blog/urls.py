from django.urls import path
from . import views

urlpatterns = [
    path('', views.postblog, name='postblog'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('home.html', views.postblog, name='postblog'),
]