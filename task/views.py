from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def add_task(request):
  task_form=forms.TaskForm()
  return render(request,'add_task.html',{'form':task_form})