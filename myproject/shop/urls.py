from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='shop-home'),
    path('product/',views.product,name='shop'),
]
