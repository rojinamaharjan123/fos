from django.urls import path
from foodapp.views import *
app_name = "foodapp"

urlpatterns= [
	# client url
	path("home/", HomeView.as_view(),name="home"),

	# admin url
	#restaurant
	path("admin/home/", 
		AdminHomeView.as_view(),name="adminhome"),
	path('admin/restaurant-create/', 
		AdminRestaurantCreateView.as_view(), name='adminrestaurantcreate'),
	path('admin/restaurant-list/', 
		AdminRestaurantListView.as_view(), name = 'adminrestaurantlist'),
	path('admin/restaurant/<int:pk>/detail/', 
		AdminRestaurantDetailView.as_view(),name = 'adminrestaurantdetail'),
	path('admin/restaurant/<int:pk>/update/', 
		AdminRestaurantUpdateView.as_view(), name = 'adminrestaurantupdate'),
	path('admin/restaurant/<int:pk>/delete/', 
		AdminRestaurantDeleteView.as_view(), name = 'adminrestaurantdelete'),
	#slider
	path('admin/slider-create/', 
		AdminSliderBannerCreateView.as_view(), name = 'adminsliderbannercreate'),
	path('admin/slider-list/', 
		AdminSliderBannerListView.as_view(), name = 'adminsliderbannerlist'),
	# path('admin/slider/<int:pk>/delete/'AdminSliderBannerDetailView.as_view(),name = 'adminsliderbannerdetail'),
	path('admin/slider/<int:pk>/update/',
	 AdminSliderBannerUpdateView.as_view(), name = 'adminsliderbannerupdate'),
	path('admin/slider/<int:pk>/delete/', 
		AdminSliderBannerDeleteView.as_view(), name = 'adminsliderbannerdelete'),

	#category
	path('admin/category-create/',
		AdminCategoryCreateView.as_view(),name ='admincategorycreate'),
	path('admin/category-list/', 
		AdminCategoryListView.as_view(),name ='admincategorylist'),
	path('admin/category/<int:pk>/update/',
	 AdminCategoryUpdateView.as_view(),name ='admincategoryupdate'),
	path('admin/category/<int:pk>/delete/', 
		AdminCategoryDeleteView.as_view(),name ='admincategorydelete'),

	#fooditem
	path('admin/fooditem-create/',
		AdminFoodItemCreateView.as_view(),name='adminfooditemcreate'),
	path('admin/fooditem-list/',
		AdminFoodItemListView.as_view(),name='adminfooditemlist'),
	path('admin/fooditem/<int:pk>/update/',
		AdminFoodItemUpdateView.as_view(),name='adminfooditemupdate'),
	path('admin/fooditem/<int:pk>/delete/',
		AdminFoodItemDeleteView.as_view(),name='adminfooditemdelete'),

	#blogpost
	path('admin/blog-create/',
		AdminBlogCreateView.as_view(),name='adminblogcreate'),
	path('admin/blog-list/',
		AdminBlogListView.as_view(),name='adminbloglist'),
	path('admin/blog/<int:pk>/detail/',
		AdminBlogDetailView.as_view(),name='adminblogdetail'),

	# path('admin/blog-list/',
	# 	AdminBlogListView.as_view(),name='adminbloglist'),
	# path('admin/blog-list/',
	# 	AdminBlogListView.as_view(),name='adminbloglist'),
	

	


	
	
	

]