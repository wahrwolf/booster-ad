from django.db import models

# Create your models here.

class User(models.Model):
	coins = models.IntegerField(default=0)
	nick = models.CharField(max_length=200)
	fullName = models.CharField(max_length=200)
	def __str__(self):
		return self.fullName

class Offer(models.Model):
	coinValue = models.IntegerField(default = 100)
	#token entspricht einem Gutscheincode für z.B. einen Online-Warenkorb ...
	token = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	def __str__(self):
		return (self.brand + ": " + self.description)

class Brand(models.Model):
	name = models.CharField(max_length=200)
	pathLogo = models.FilePathField(path="./logos/") #TODO: change to imagefield
	website = models.URLField(max_length=200)
	description = models.CharField(max_length=200)

	def __getCategory__(self): #TODO return best matching categroy according to tags
		return -1

	def __getImgTag__(self):
		#TODO build image tag with path logo
		return "<img src='" + self.pathLogo + "' alt='" + self.name +"'/>"

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=20)
	color = models.CharField(max_length=7)
	font = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class UserPreference(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	accepted = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	
	def __str__(self):
		return (self.tag.name + "@" + self.user.nick )

class OfferTags(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
	
	def __str__(self):
		return (self.tag.name + "@" + self.offer.token +":"+self.offer.brand)

class BrandTags(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	def __str__(self):
		return (self.tag.name + "@" +self.brand.name)


