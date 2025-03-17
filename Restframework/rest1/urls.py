from django.urls import path
from rest1 import views
from django.conf.urls.static import static

urlpatterns = [
 path('',views.index,name="index"),
]