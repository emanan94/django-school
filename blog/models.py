from django.db import models
from django.utils import timezone

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


    def __str__(self):
        return self.title
