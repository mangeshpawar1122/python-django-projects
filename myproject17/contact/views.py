from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def contact(request):
  return render(request,'contact/contact.html')

def submit(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    masseges = request.POST.get('masseges')
    if name and masseges:
      Contact.objects.create(name=name, masseges=masseges)
      return HttpResponse(f"Thank You {name} form your massege!")  
    else:
      return HttpResponse(f"Plase provide both name and massege. ",status = 400)
  return render(request,'contact')