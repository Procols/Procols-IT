from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seo', views.seo, name='seo'),
    path('service', views.service, name='service'),
    path('webapp', views.webapp, name='webapp'),
    path('digitalmarketing', views.digitalmarketing, name='digitalmarketing'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus')
]