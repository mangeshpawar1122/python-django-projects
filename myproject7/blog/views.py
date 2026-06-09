from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
  blogs = [
    {"title":'django Basic','is_featured':True,"author":'Pawar Mangesh'},
    {"title":'django Advanced','is_featured':False,"author":''},
    {"title":'django web fremwork','is_featured':False,"author":'Pawar kajal'},
  ]

  context = {
    'blog':blogs,
    'todays':datetime.now(),
    'html_code':'<b>welcome to my blog</b>',

  }
  return render(request,'blog/home.html',context)