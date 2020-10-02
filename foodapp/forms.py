from django import forms
from .models import *


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = "__all__"
		widgets = {
		'name': forms.TextInput(attrs={
			'class' :  'form-control',
			'placeholder':'Enter the Restaurant name',
		}),
		'logo' :  forms.ClearableFileInput(attrs={
			'class': 'form-control'
		}),

		'email' :forms.TextInput(attrs = {
			'class' : 'form-control',
			'placeholder' : 'Enter Email'
		}),
		'phone':forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder':'Enter the Phone Number',
		}),
		'address' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Address',
		}),
		'about' : forms.Textarea(attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter About Restaurant',
			'rows' : '3'
		}),
		'map_location' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Map Location',
		}),
		'facebook' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Facebook Link',
		}),
		'instagram' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Instagram Link',
		}),
		'youtube' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Youtube Link',
		}),
		'twitter' : forms.TextInput(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter Twitter Link',
		}),
		
		}


class SliderBannerForm(forms.ModelForm):
	class Meta:
		model = SliderBanner
		fields = "__all__"
		widgets = {
		'title' :forms.TextInput(attrs = {
			'class' : 'form-control',
			'placeholder' : 'Enter Title'
		}),
		'caption' : forms.Textarea(attrs={
			'class' :'form-control',
			'placeholder' : 'Enter placeholder',
			'rows': '3',
		}),
		'image' :  forms.ClearableFileInput(attrs={
			'class': 'form-control'
			})
		}


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = "__all__"
		widgets = {
		'title': forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter Title'
			}),
		'description': forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Enter Description',
			'rows': '5',
			})
		}

class FoodItemForm(forms.ModelForm):
	class Meta:
		model = FoodItem
		fields = "__all__"
		widgets = {
		'name': forms.TextInput(attrs={
			'class' :  'form-control',
			'placeholder':'Enter the FoodItem name',

			}),
		'category': forms.Select(attrs={
			'class' : 'form-control',
			'placeholder' : 'Select Category'
			}),
		'photo' : forms.ClearableFileInput(attrs={
			'class' : 'form-control'
			}),
		'price':forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder':'Enter the Price',
			}),
		'description' : forms.Textarea(attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter FoodItem Description',
			'rows' : '3'
			}),
		
		}


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = "__all__"
		widgets = {
		'title' : forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter the Blog title'
			}),
		'description' : forms.Textarea(attrs={
			'class' : 'form-control',
			'placeholder' : 'Enter Blog Desciption',
			'rows' : '9'
			}),
		'image': forms.ClearableFileInput(attrs={
			'class' : 'form-control'
			}),
		}


