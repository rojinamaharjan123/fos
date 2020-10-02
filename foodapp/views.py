from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy, reverse
from .models import *

# get, get_context_data, form_valid, dispatch

# Create your  client views here.
class HomeView(TemplateView):
	template_name="clienttemplates/clienthome.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['restaurant'] = Restaurant.objects.first()
		# print(restaurant, '\n ++++++++++++++++++++++++++++++')
		context['sliderbannerlist'] = SliderBanner.objects.all()
		context['categoryname'] = Category.objects.all()

		return context
	
#create your admin view	here
class AdminHomeView(TemplateView):
	template_name = "admintemplates/adminhome.html"

# restaurant 	
class AdminRestaurantCreateView(CreateView):
	template_name = "admintemplates/restaurantcreate.html"
	form_class = RestaurantForm
	success_url = reverse_lazy("foodapp:adminhome")

class AdminRestaurantListView(ListView):
	template_name ="admintemplates/restaurantlist.html"
	queryset = Restaurant.objects.all()
	context_object_name = "restaurantlist"

class AdminRestaurantDetailView(DetailView):
	template_name = "admintemplates/restaurantdetail.html"
	model = Restaurant
	context_object_name = "restaurantdetail"

class AdminRestaurantUpdateView(UpdateView):
	template_name = "admintemplates/restaurantcreate.html"
	form_class = RestaurantForm
	success_url = reverse_lazy("foodapp:adminhome")
	model = Restaurant

class AdminRestaurantDeleteView(DeleteView):
	template_name = "admintemplates/restaurantdelete.html"
	success_url = reverse_lazy("foodapp:adminhome")
	model = Restaurant

#slider
class AdminSliderBannerCreateView(CreateView):
	template_name = "admintemplates/sliderbannercreate.html"
	form_class = SliderBannerForm
	success_url = reverse_lazy("foodapp:adminhome")

class AdminSliderBannerListView(ListView):
	template_name = "admintemplates/sliderbannerlist.html"
	queryset = SliderBanner.objects.all()
	context_object_name = "sliderbannerlist"

class AdminSliderBannerUpdateView(UpdateView):
	template_name = "admintemplates/sliderbannercreate.html"
	form_class = SliderBannerForm
	success_url = reverse_lazy("foodapp:adminhome")
	model = SliderBanner


class AdminSliderBannerDeleteView(DeleteView):
	template_name = "admintemplates/sliderbannerdelete.html"
	model = SliderBanner
	success_url = reverse_lazy("foodapp:adminhome")

#Categoryview

class AdminCategoryCreateView(CreateView):
	form_class = CategoryForm
	template_name = "admintemplates/categorycreate.html"
	success_url = reverse_lazy("foodapp:adminhome")

class AdminCategoryListView(ListView):
	template_name = "admintemplates/categorylist.html"
	queryset = Category.objects.all()
	context_object_name = "categorylist"

class AdminCategoryUpdateView(UpdateView):
	template_name = "admintemplates/categorycreate.html"
	form_class = CategoryForm
	success_url = reverse_lazy("foodapp:admincategorylist")
	model  = Category

class AdminCategoryDeleteView(DeleteView):
	template_name = "admintemplates/categorydelete.html"
	model = Category
	success_url = reverse_lazy("foodapp:admincategorylist")
	
#fooditemview

class AdminFoodItemCreateView(CreateView):
	template_name = "admintemplates/fooditemcreate.html"
	form_class = FoodItemForm
	success_url = reverse_lazy("foodapp:adminhome")

class AdminFoodItemListView(ListView):
	template_name = "admintemplates/fooditemlist.html"
	queryset = FoodItem.objects.all()
	context_object_name = "fooditemlist"

class AdminFoodItemUpdateView(UpdateView):
	template_name = "admintemplates/fooditemcreate.html"
	form_class = FoodItemForm
	model = FoodItem
	success_url =reverse_lazy("foodapp:adminfooditemlist")

class AdminFoodItemDeleteView(DeleteView):
	template_name = "admintemplates/fooditemdelete.html"
	model = FoodItem
	success_url = reverse_lazy("foodapp:adminfooditemlist") 


#BLog

class AdminBlogCreateView(CreateView):
	template_name = 'admintemplates/blogcreate.html'
	form_class = BlogForm
	success_url = reverse_lazy('foodapp:adminhome')


class AdminBlogListView(ListView):
	template_name = 'admintemplates/bloglist.html'
	queryset = Blog.objects.all()
	context_object_name = 'bloglist'

class AdminBlogDetailView(DetailView):
	template_name = 'admintemplates/blogdetail.html'
	model = Blog
	context_object_name = 'blogdetail'

