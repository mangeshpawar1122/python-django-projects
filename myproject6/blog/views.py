from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
  post = {
    "title":"My Second Templates Post",
    "Discriptions": "django is a high level web fremwork",
    "author": None,
    "created_at":datetime(2026,6,6,6,40),
    "comments_counts":5,
    "tags":["django","python","web-development"],
    "numbers":8,
    "price":100,
  }
  return render(request,'blog/home.html',{"post":post})