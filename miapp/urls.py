from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/',views.prueba,name="prueba"),
    path('',views.landing,name="landing")
]