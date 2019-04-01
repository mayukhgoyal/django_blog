from django.urls import  path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)	
from . import views
# Defining URL here of all
urlpatterns = [
    path('',views.home, name='movie1-home'),
    path('',PostListView.as_view(), name='movie1-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
		path('post/new/',PostCreateView.as_view(),name="post-create"),
		path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
		path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='movie1-about'),
    path('contact/',views.contact, name='movie1-contact'),
    path('profile/',views.profile, name='movie1-profile'),
]
