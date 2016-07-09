from django.conf.urls import url

from . import views

app_name = 'offers'
urlpatterns = [
	# ex: /offers/
	url(r'^$', views.index, name='index'),
	# ex: /offers/user/2
	url(r'^user/(?P<userId>[0-9]+)/$', views.profile, name='profile'),
	# ex: /offers/user/2/shop
	url(r'^user/(?P<userId>[0-9]+)/shop/$', views.shop, name='shop'),
	
	# ex: /offers/card/random
	url(r'^card/random/$',views.getOffer, name ='newCard'),

	# ex: /offers/populate
	url(r'^populate/$', views.populate, name = 'populate'),
]
