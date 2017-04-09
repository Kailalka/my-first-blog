
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^kai/$', views.main, name='main'),
	url(r'^posts/$', views.post_list, name='list'),
	url(r'^posts/(?P<post_id>\d+)/$', views.post_detail, name='detail'),
]
