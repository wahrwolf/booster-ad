from django.db import models

# Create your models here.

class User(models.Model):
	DEFAULT_PK=-1
	coins = models.IntegerField(default=0)
	nick = models.CharField(max_length=200)
	fullName = models.CharField(max_length=200)
	def __str__(self):
		return self.fullName
class Brand(models.Model):
	name = models.CharField(max_length=200)
	pathLogo = models.FilePathField(path="/tmp/logos/") #TODO: change to imagefield
	website = models.URLField(max_length=200)
	description = models.CharField(max_length=200)

	def __getCategory__(self): #TODO return best matching categroy according to tags
		return -1

	def __getImgTag__(self):
		#TODO build image tag with path logo
		return "<img src='" + self.pathLogo + "' alt='" + self.name +"'/>"

	def __str__(self):
		return self.name


class Offer(models.Model):
	coinValue = models.IntegerField(default = 100)
	#token entspricht einem Gutscheincode für z.B. einen Online-Warenkorb ...
	token = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, default="open")
	correspondant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=User.DEFAULT_PK)
	def __str__(self):
		return (str(self.brand) + ": " + self.token)

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

class UserTag(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	accepted = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	
	def __str__(self):
		return (self.tag.name + "@" + self.user.nick )

class OfferTag(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
	
	def __str__(self):
		return (self.tag.name + "@" + self.offer.token +":"+str(self.offer.brand))

class BrandTag(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	def __str__(self):
		return (self.tag.name + "@" +self.brand.name)


