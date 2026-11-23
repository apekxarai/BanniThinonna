
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sweets/', views.sweets, name='sweets'),
    path('sweets/<int:sweet_id>/', views.sweet_detail, name='sweet_detail'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cakes/', views.cakes, name='cakes'),
    path('cake/<int:cake_id>/', views.cake_detail, name='cake_detail'),
    path('namkeens/', views.namkeens, name='namkeens'),
    path('namkeen/<int:id>/', views.namkeen_detail, name='namkeen_detail'),
]