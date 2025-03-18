from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Service
from .forms import ServiceForm
from django.contrib import messages
# My  views or logic of the system.
def index(request):

    return render(request,'rest1/layout.html')

def service_list(request):
    # Fetch all services from the database
    services = Service.objects.all()
    # Render the 'service_list.html' template with the services context
    return render(request, 'rest1/service.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'rest1/service_detail.html', {'service': service})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service added successfully!")
            return redirect('service_list')  # Redirect to the service list page after saving the service
    else:
        form = ServiceForm()

    return render(request, 'rest1/add_service.html', {'form': form})