from django.contrib import admin
from .models import *

admin.site.register([Restaurant, SliderBanner, Category, FoodItem, Blog, Subscription, Comment])

# Register your models here.
