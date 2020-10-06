from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
post_type = [
    ('draft' ,'draft'),
    ('published' , 'published')
]

class Post(models.Model): #db table
    title = models.CharField(max_length=50 , unique=True) #db colomn
    content = models.TextField(max_length=2000 , null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default = False)
    author_mail = models.EmailField(default='')
    typee = models.CharField(choices=post_type ,default='draft', max_length=20 )
    image = models.ImageField(upload_to = 'post/' )


    class Meta: #to customize
        verbose_name = 'Posttt'
        verbose_name_plural='postoo'
        ordering=('title',) #tuple
        #ordering=('-title',) #to reverse

       # db_table='' #to change model name in db

    
    def __str__(self):
        return self.title

    
    #isntance method
    def get_read_time(self):
        pass

    #instance method 
    def get_absolute_url(self):
        return reverse("blog:cbv_detail" ,kwargs={"pk":self.pk})




class Ccomment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #db relationships
    text = models.TextField(max_length=200)


    def __str__(self):
        return str(self.post) 
