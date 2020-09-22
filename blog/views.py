from django.shortcuts import render,redirect,reverse
from .models import Post
from .forms import PostForm

# Create your views here.

#show all posts
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