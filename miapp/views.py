from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
# Create your views here.
def prueba(request):
    return HttpResponse("esta es mi prueba")