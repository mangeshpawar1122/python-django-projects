from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
  def __init__(self,name , age):
    self.name = name,
    self.age = age
def home(request):
  context = {
    "name":"mangesh pawar",
    "age":23,
    "skills":["python","django","mysql","react"],
    "user":User('kajal' ,22),
    "blog":{
      "title":"Django templates introduction",
      "Author":{
        "fullname":"Mangesh Pawar"
      },
      "content":"<b>this is bold</b>",
      "created_at":datetime(2026,6,6,14,40)
    },
    "empty_value":None,
  }    
  return render(request,'shop/home.html',context)
