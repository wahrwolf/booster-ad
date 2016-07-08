from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(OfferTag)
admin.site.register(BrandTag)
admin.site.register(UserTag)
