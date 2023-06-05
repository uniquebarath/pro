from django.http import HttpResponse
from django.shortcuts import render
from .models import*

def app_index(request):
    return render(request,'app_index.html')

def datas(request):
    if request.method =="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        place=request.POST.get('place','')
        college=request.POST.get('college','')
        address=request.POST.get('address','')
        forms= form(name=name, email=email, number=number ,place=place, college=college, address=address)
        forms.save()

    return render(request,'app1/form.html')

# Create your views here.
