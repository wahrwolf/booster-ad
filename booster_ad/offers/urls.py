from django.conf.urls import url

from . import views

app_name = 'offers'
urlpatterns = [
	# ex: /offers/
	url(r'^$', views.index, name='index'),
	url(r'^user/(?P<userId>[0-9]+)/$', views.profile, name='profile'),
	url(r'^user/(?P<userId>[0-9]+)/shop/$', views.shop, name='shop'),
]
