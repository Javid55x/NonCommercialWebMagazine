from django.urls import path
from . import views
from .views import IndexView, AboutView, ContactView, ProductListView, ProductDetailView, ShowRoomView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('show-room', ShowRoomView.as_view(), name='show-room'),
    path('search/', views.search, name='search'),
]
