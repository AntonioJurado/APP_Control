from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^data$', views.data, name='data'),
	#url(r'^sensors/(?P<pk>[\d]+)/$', views.results, name='results'),
	url(r'^/$', views.index, name='detail'),
]