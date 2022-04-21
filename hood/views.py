
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Profile, Neighborhood
from .forms import CreateBusiness, CreateService, UserRegistrationForm, LoginUserForm, CreateJoinHoodForm, CreatePost

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('home', hood=request.user.profile.hood.neighborhoodName)
    return render(request, 'index.html')


def signupUser(request):
    if request.user.is_authenticated:
       return redirect(createJoinHood)

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        user = form.save(commit=False)
        if form.is_valid():
            if User.objects.filter(username=user.username.lower()).exists():
                messages.error(
                    request, f'A User with the username, {user.username}, Already exists')
            elif User.objects.filter(email=user.email.lower()).exists():
                messages.error(
                    request, f'A user with the email, {user.email}, Already exists')
            else:
                user.email = user.email.lower()
                user.username = user.username.lower()
                user.save()
                userProfile = Profile(user=user)
                userProfile.save()
                login(request, user)
                return redirect(createJoinHood)

    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('create-join-hood')

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            try:
                user_exist = User.objects.get(username=username)
                if user_exist:
                    user = authenticate(
                        request, username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect('create-join-hood')
                    else:
                        messages.error(request, 'Invalid username or password')
            except:
                messages.error(request, 'User does not exist, sign-up')

    form = LoginUserForm()
    context = {'form': form}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect(loginUser)


@login_required(login_url='login')
def home(request, hood):
    form = CreatePost()

    neighborhood = Neighborhood.objects.get(neighborhoodName = hood)

    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            newPost = form.save(commit = False)
            newPost.hood = neighborhood
            newPost.postedBy_id = request.user.id
            newPost.save()
            messages.success(request, 'Post Added Successfully')
        else:
            messages.error(request, 'An Error Occurred while uploading your post')
    print(request.user.profile.hood)
    posts = neighborhood.posts.all()
    for post in posts:
        print(post.postedBy)
    context = {'posts': posts, 'form': form}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def createJoinHood(request):

    neighborhoods = Neighborhood.objects.all()
    print(neighborhoods)

    if request.user.is_authenticated and request.user.profile.hood:
        hoodName = request.user.profile.hood.neighborhoodName
        return redirect(home, hoodName)
    
    form = CreateJoinHoodForm()
    context = {'form': form, 'neighborhoods': neighborhoods}
    return render(request, 'create_join_hood.html', context)

@login_required(login_url='login')
def createHood(request):
    userProfile = Profile.objects.get(user=request.user) 
    if request.method == 'POST':
        form = CreateJoinHoodForm(request.POST)
        if form.is_valid():
            newHood = form.save(commit=False)
            newHood.creator = request.user
            newHood.save()
            userProfile.hood = newHood
            userProfile.save()
            return redirect(home, hood = newHood.neighborhoodName)
        
        else:
            return redirect(createJoinHood)


@login_required(login_url='login')
def joinHood(request):
    print('being called...')
    if request.method == 'POST':
        hoodObj = request.POST.dict()
        hoodName = hoodObj.get('hoodName')

        hood = Neighborhood.objects.get(neighborhoodName = hoodName)
        userProfile = Profile(user = request.user)
        userProfile.hood = hood
        userProfile.save()
        
        return redirect(home, hood= hoodName)

@login_required(login_url='login')
def service(request, hood):
    hood = Neighborhood.objects.get(neighborhoodName = hood)
    services = hood.services.all()
    print(services)

    if request.method == 'POST':
        form = CreateService(request.POST)
        if form.is_valid():
            newService = form.save(commit=False)
            newService.neighborhood = hood
            newService.save()
            messages.success(request, 'Service Added Successfully')
        else:
            messages.error(request, 'An Error occurred while creating a service...')

    form = CreateService()
    context = {'form': form, 'services': services}
    return render(request, 'services.html', context)


@login_required(login_url='login')
def business(request, hood):
    hood = Neighborhood.objects.get(neighborhoodName=hood)
    businesses = hood.businesses.all()

    if request.method == 'POST':
        form = CreateBusiness(request.POST)
        if form.is_valid():
            newBusiness = form.save(commit=False)
            newBusiness.neighborhood = hood
            newBusiness.businessOwner = request.user
            newBusiness.save()
            messages.success(request, 'Business Added Successfully')


    form = CreateBusiness()
    context = {'form': form, 'businesses': businesses}
    return render(request, 'business.html', context) 