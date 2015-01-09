from django.conf.urls import patterns, url
from mblog import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^post/', views.post, name='post'),
	url(r'^post/(?P<post_title_slug>[\w\-]+)/$', views.post, name='post'),)  # New!