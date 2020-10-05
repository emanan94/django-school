from django.shortcuts import render,redirect,reverse
from .models import Post
from .forms import PostForm
from django.db import models
from django.views.generic import ListView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

#Class based view(cbv)

class PostList(ListView):
#class PostList(LoginRequiredMixin,ListView): #mixins to make sure that no one could see page without login with cbv
    model = Post
    template_name = 'post/blog/post_list.html' 
    #template_name = 'post/all_posts.html' # to use the same html page from all_posts function


class PostDetail(DeleteView):
    model = Post
    template_name = 'post/blog/post_detail.html'

class PostUpdate(UpdateView):
    model = Post
    template_name = 'post/blog/post_form.html'
    fields = ['title','content'] # to use the form
    success_url = '/blog/cbv'



#function based view(FBV)
#show all posts

#@login_required  #decorator to make sure that no one could see page without login with Fbv
def all_posts(request):
    all_posts =Post.objects.all()
   
    return render(request , 'post/all_posts.html' ,{'posts':all_posts} )

#show single post
def single_post(request,id):
    single_post = Post.objects.get(id=id)
    return render(request , 'post/single_post.html' ,{'post':single_post} )

#add post
def new_post(request):
  #  print('nnn') # to test data
    if request.method=='POST':
        form = PostForm(request.POST , request.FILES) #Request.files to recieve data (audio, imgs, videos)
        if form.is_valid():
           form.save()
           return redirect(reverse('blog:blog_list'))
    else:
        form = PostForm()
    return render(request, 'post/new.html' , {'form':form})

#Edit post
# def post_edit(request,id):
#     if request.method=='POST':
#         form = PostForm(request.POST,request.FILES) #Request.files to recieve data (audio, imgs, videos)
#         if form.is_valid():
#            form.save()
#            return redirect(reverse('blog:blog_list'))
#     else:
#         form = PostForm()#(instance=single_post)
#     return render(request, 'post/new.html' , {'form':form})
