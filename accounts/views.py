from django.shortcuts import render,redirect,reverse
from .models import Profile
from .forms import UserForm,ProfileForm,UserCreateForm
from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    if request.method=='POST':
        signup_form=UserCreateForm(request.POST) #request.POST to save data
        if signup_form.is_valid():
            signup_form.save()
            username=signup_form.cleaned_data['username']
            password=signup_form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))    
    else:
        signup_form=UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form })



def profile(request):
    profile=Profile.objects.get(user=request.user) # to show data of current user data 
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile=Profile.objects.get(user=request.user)       # to show data of current user data 
    if request.method=='POST':
        user_form=UserForm(request.POST ,instance=request.user)                 # to show POSTED data from user  // this instance after editting
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)  # to show POSTED data from profile //  request.FILES for Media files //this instance after editting

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()    
            return redirect(reverse('accounts:profile'))      #namespade of app :name of direction 
    else:
        user_form=UserForm(instance=request.user)        # instance to show data from user
        profile_form=ProfileForm(instance=profile)       # instance to show data from profile
    return render(request,'profile/profile_edit.html',{
        'user_form':user_form,                           # 'user_form' to call it in html page 
        'profile_form':profile_form
        })


   