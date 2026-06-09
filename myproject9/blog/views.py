from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request,'blog/home.html')

def base(request):
  student_list = [
    {"name":"Mohit","class":'10th'},
    {"name":"Rohit","class":'9th'},
    {"name":"Sohit","class":'8th'},
  ]
  return render(request,'base.html',{"student":student_list})