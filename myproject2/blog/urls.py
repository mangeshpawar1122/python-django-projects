from . import views
from django.urls import path,re_path

urlpatterns = [
    path('post/<int:post_id>/',views.post_deatils, name='post_deatils'),# this is a integer type path ex = 1.1.1.8080/blog/id=1/
    path('user/<str:username>/',views.user_deatils,name='user_deatils'), # this id is string type path ex = 1.1.1.8080/blog/name/
    path('article/<int:year>/<int:month>/<int:days>/',views.article_details,name='article_details'), # this is **kwargs type ex = 1.1.1.8080/blog/article/2002/12/20

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year,name='article_by_year'), # this is a re_path types ex = 1.1.1.8080/blog/article/2002


]
