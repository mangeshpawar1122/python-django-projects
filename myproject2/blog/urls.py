from . import views
from django.urls import path,re_path

urlpatterns = [
    path('post/<int:post_id>/',views.post_deatils, name='post_deatils'),
    path('user/<str:username>/',views.user_deatils,name='user_deatils'),
    path('article/<int:year>/<int:month>/<int:days>/',views.article_details,name='article_details'),

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year,name='article_by_year'),


]
