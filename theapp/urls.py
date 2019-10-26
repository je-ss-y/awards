from django.conf.urls import url
from . import views

urlpatterns=[
    url('^today/$',views.posts_of_day,name='postsToday')
]