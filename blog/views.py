from django.shortcuts import render
from .models import Post

# Create your views here.

#show all posts
def all_posts(request):
    all_posts =Post.objects.all()
   
    return render(request , 'post/all_posts.html' ,{'posts':all_posts} )

#show single post
def single_post(request,id):
    single_post = Post.objects.get(id=id)
    return render(request , 'post/single_post.html' ,{'post':single_post} )