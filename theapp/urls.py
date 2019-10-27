from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^today/$',views.posts_of_day,name='postsToday'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^profileform', views.profile_form, name='profile'),
    # url(r'^profiledisplay', views. user_profile, name='profiledisplay'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)