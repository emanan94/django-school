from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:       #to define form
        model = Post 
     #   fields = '__all__' 

     #  fields = ['content','image'] #to show specific fields

        exclude = ['created_at',]  # with " , " its a list , without it its a string  #to show all except one field
        
       