from django.contrib import admin
from .models import User, Offer, Brand, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Brand)
admin.site.register(Category)
