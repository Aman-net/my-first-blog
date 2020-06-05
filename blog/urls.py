from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html/', views.about, name='about'),
    path('contact.html/', views.contact, name='contact'),
    path('home.html/', views.home, name='home'),
    path('post/new/', views.post_new, name='post_new'),
]