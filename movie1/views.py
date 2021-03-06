from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView 
)	
from .models import Post
# Home page 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'home.html',context)
class PostListView(ListView):
	model = Post
	template_name = 'movie1/home.html'	# <app>/<model>_<viewtype>.html
	context_object_name = 'posts'	
	ordering = ['-date_posted']
class PostDetailView(DetailView):
	model = Post	
	#import pdb; pdb.set_trace();
	template_name = 'post_detail.html'
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post	
	fields = ['title','content']
	template_name = 'post_create.html'
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'post_create.html'
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			  return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'post_confirm_delete.html'
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			 return True
		return False	 

# About Page
def about(request):
    return render(request,'about.html',{'title':'About'})
# Contact Page
def contact(request):
    return render(request,'contact.html',{'title':'Contact'})
# Profile page
def profile(request):
    return render(request,'profile.html',{'title':'Profile'})