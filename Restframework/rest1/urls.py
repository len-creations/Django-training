from django.urls import path
from rest1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('',views.index,name="index"),
 path('services/', views.service_list, name='service_list'),
 path('add service/', views.add_service, name='add_service'),
 path('/<slug>/',views.service_detail,name='service_detail'),
]
