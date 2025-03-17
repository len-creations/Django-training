from django.shortcuts import render
from django.contrib.auth.models import User

# My  views or logic of the system.
def index(request):

    return render(request,'rest1/layout.html')