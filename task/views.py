from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def add_task(request):
  if request.method=='POST':
    task_form=forms.TaskForm(request.POST)
    if task_form.is_valid():
      # print(task_form.cleaned_data)
      task_form.save()
  else:
    task_form=forms.TaskForm()
  return render(request,'add_task.html',{'form':task_form})