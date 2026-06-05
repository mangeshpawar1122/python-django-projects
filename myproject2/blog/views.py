from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_deatils(request,post_id):
  return HttpResponse(f'<h1>show blog in {post_id} </h1>')


def user_deatils(request,username):
  return HttpResponse(f"<h1> this is a {username} </h1>")


def article_by_year(request, year):
  return HttpResponse(f' <h1> this is a year {year} </h1>')

def article_details(request,**kwargs):
  return HttpResponse(f'this is a Data:{kwargs}')