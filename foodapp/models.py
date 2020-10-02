from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True , null =True, blank =True)
	is_active = models.BooleanField(default = True , null =True ,blank = True)

	class Meta:
		abstract = True

class Customer(TimeStamp):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	email = models.EmailField()
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	
class Restaurant(TimeStamp):
	name = models.CharField(max_length =100)
	logo = models.ImageField(upload_to = "restaurant")
	email = models.EmailField()
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	about = models.TextField()
	map_location = models.CharField(max_length=200)
	facebook = models.CharField(max_length = 200, null=True, blank=True)
	instagram = models.CharField(max_length = 200, null=True, blank=True)
	twitter = models.CharField(max_length = 200, null=True, blank=True)
	youtube = models.CharField(max_length = 200, null=True, blank=True)

	def __str__(self):
		return self.name


class SliderBanner(TimeStamp):
	title = models.CharField(max_length=300)
	caption = models.TextField()
	image = models.ImageField(upload_to="slider")

	def __str__(self):
		return self.title


class Category(TimeStamp):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title


class FoodItem(TimeStamp):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to = "foodimg")
	price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
	description = models.TextField()
	views = models.PositiveIntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.name

class Blog(TimeStamp):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	image = models.ImageField(upload_to="blogimg")

	def __str__(self):
		return self.title

class Subscription(TimeStamp):
	email = models.EmailField()

	def __str__(self):
		return self.email

class Comment(TimeStamp):
	content = models.CharField(max_length=100)
	commenter = models.CharField(max_length=100)
	blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

	def __str__(self):
		return self.commenter



