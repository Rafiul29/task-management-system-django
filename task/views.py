from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add_task(request):
  return render(request,'add_task.html')