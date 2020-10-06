from django.contrib import admin

# Register your models here.
from .models import Post ,Ccomment


class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','typee','active']
    list_filter  =['typee', 'active']
    search_fields=['title','content']


admin.site.register(Post ,PostAdmin) #second parameter to nconnect it with first one
admin.site.register(Ccomment)