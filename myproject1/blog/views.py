from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
  return HttpResponse('<h1>this is a sencond blon in second home page</h1>')


def about(request):
  lst = [2,4,2,45,7,6,2,8,5]
  emty = [ ]
  for i in lst:
    if i not in emty:
      emty.append(i)
  return HttpResponse(f'all those value is unic {emty}')
