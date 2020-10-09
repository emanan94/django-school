from django.urls import path
from .views import profile, profile_edit


app_name ='accounts'

urlpatterns=[
    #page link , template name in view , name)
    path('profile/',profile,name='profile'),
    path('profile/edit',profile_edit, name='profile_edit')
]