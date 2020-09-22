
from django.urls import path
from blog.views import all_posts , single_post , new_post #have to import functions to declare 

app_name='blog'

urlpatterns = [
    path('' , all_posts , name='blog_list'),
    path('<int:id>',single_post, name='blog_detail'),
    path('new' , new_post , name='new_post') #new is a name of html page
]
