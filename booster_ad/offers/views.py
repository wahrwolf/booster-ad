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
	brands = Brand.objects.all()

	return render(request, 'offers/index.html',{'brands' : brands})

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
		entries= []
		#User
		tom = User.objects.create(nick="tommy", fullName = "Tom Schmidt", coins=100)
		tanja = User.objects.create(nick="tanja", fullName = "Tanja Witz", coins=100)

		entries.extend((tanja, tom))

		#Brand
		bringerando = Brand.objects.create(name="bringerando", pathLogo="pizza.jpg", website = "www.bringerando.de", description = "Essen wann du willst, wen du willst")
		xlando = Brand.objects.create(name="xlando", pathLogo="shoe.jpg", website = "www.xlando.de", description = "Schrei vor Freude")
		clizzard= Brand.objects.create(name="clizzard", pathLogo="controller.jpg", website = "www.clizzard.com", description = "Make Games great again!")

		entries.extend((bringerando, xlando, clizzard))


		for i in entries:
			i.save()

	#Offer
		shoes = Offer.objects.create(coinValue = 1400, description ="Get 3 for 2", token="3FORETw0", brand = xlando)
		beta = Offer.objects.create(coinValue= 50, description = "Closed Beta-Access", token="UnderWatchBeta", brand =clizzard)
		pizza = Offer.objects.create(coinValue=750, description="Get a free pizza", token ="freeP1zzA", brand = bringerando)
		entries.extend((shoes, beta, pizza))

		return HttpResponse("<h1>Import done:</h1>")
	else:
		return HttpResponseForbidden()
