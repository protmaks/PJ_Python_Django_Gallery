from django.urls import path
from .views import (ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView, ImageDeleteView, UserImageListView, SearchResultsView)
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('gallery/', ImageListView.as_view(), name='gallery'),
	path('search/', SearchResultsView.as_view(), name='search_results'),
	path('user/<str:username>', UserImageListView.as_view(), name='user-images'),
	path('about/', views.about, name='gallery-about'),
	path('gallery/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
	path('gallery/new/', ImageCreateView.as_view(), name='image-create'),
	path('gallery/<int:pk>/update/', ImageUpdateView.as_view(), name='image-update'),
	path('gallery/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
]