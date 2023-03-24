from django import urls
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('home/', BookList.as_view(), name='home'),
    path('details-book/<int:pk>/', BookDetail.as_view(), name='details'),
    path('account/<int:pk>/',Account.as_view(), name='account'),
    # path('complete',views.PaymentComplete),
    path('search/',SearchResult.as_view(),name="search"),
    path('checkout/', views.checkOut, name="checkout"),
    path('cart/', views.cart, name='cart')

]
