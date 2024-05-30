from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def add_category(request):
  category_form=forms.CategoryForm()
  return render(request,'add_category.html',{'form':category_form})
