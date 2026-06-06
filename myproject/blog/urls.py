from . import views
from django.urls import path

urlpatterns = [
  path('', views.home, name='blog-home'), # this is a normal urls ex = blog/
  path('about/', views.about, name='blog-about'), # blog/about/
]