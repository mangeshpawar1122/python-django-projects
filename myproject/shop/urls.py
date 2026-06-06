from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='shop-home'),  # ex = 1.1.2.8080/shop/
    path('product/',views.product,name='shop'), # 2020/shop/product
]
