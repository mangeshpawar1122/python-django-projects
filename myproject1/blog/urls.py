from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),# dairect show ex = 1.1.1.8080/ open this urls
    path('about/',views.about,name='about'), # ex  = 1.1.1.8080/about/
]
