from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings

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
	offers = Offer.objects.all()
	return HttpResponseForbidden()

def populate(request):
	if settings.DEBUG:
		return HttpResponse("<h1>Import done ...</h1>")
	else:
		return HttpResponseForbidden()
