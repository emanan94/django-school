
from django.urls import path
from blog.views import all_posts , single_post , new_post, PostList, PostDetail,PostUpdate  #have to import functions to declare 


app_name='blog'

urlpatterns = [
    path('' , all_posts , name='blog_list'),
    path('new' , new_post , name='new_post'),  #new is a name of html page
    path('<int:id>',single_post, name='blog_detail'),
    #path('<int:id>/edit',post_edit, name='post_edit'),

    path('cbv',PostList.as_view()), # as_view used cause url take only function
    path('cbv/<int:pk>',PostDetail.as_view()),
    path('cbv/<int:pk>/edit',PostUpdate.as_view())
]
