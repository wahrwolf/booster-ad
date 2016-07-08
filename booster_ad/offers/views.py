from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User
# Create your views here.

def index(request):
	return render(request, 'offers/index.html',{})

def profile(request, userId):
	user = get_object_or_404(User, pk=userId)
	return render(request, 'offers/profile.html', {'user':user})

def shop(request, userId):
	user = get_object_or_404(User, pk=userId)
	return HttpResponse("<p>No such bay</p>")
