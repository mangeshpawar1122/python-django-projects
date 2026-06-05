from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

  return HttpResponse("<h1> wellcome to the home blog app</h1>")


def about(request):
  a = 5
  b = 10

  c = a + b
  return HttpResponse(f'<h3>this is a addition in django</h3> <h1>{c}</h1>')