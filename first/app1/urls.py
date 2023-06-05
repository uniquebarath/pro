from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app_index),
    path('form/',datas)
]