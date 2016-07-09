from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.conf import settings

from random import randint

##Use for production
#from .models import User, Offer

##Use for testing
from .models import *

# Create your views here.

def index(request):
	return render(request, 'offers/index.html',{})

def profile(request, userId):
	user = get_object_or_404(User, pk=userId)
	return render(request, 'offers/profile.html', {'user':user})

def shop(request, userId):
	user = get_object_or_404(User, pk=userId)
	return HttpResponse("<p>No such bay</p>")

def getOffer(request):
	offers = Offer.objects.filter(status="open").values('description','coinValue', 'brand')
	if offers.count() > 0:
		offer = offers[randint(0,offers.count()-1)]
		return JsonResponse(offer)
	else:
		return HttpResponseForbidden() #TODO find some better error ...

def populate(request):
	if settings.DEBUG:
		return HttpResponse("<h1>Import done ...</h1>")
	else:
		return HttpResponseForbidden()
