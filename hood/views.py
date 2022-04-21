from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Profile, Neighborhood
from .forms import UserRegistrationForm, LoginUserForm, createJoinHoodForm

# Create your views here.


def index(request):
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
    pass

@login_required(login_url='login')
def createJoinHood(request):

    neighborhoods = Neighborhood.objects.all()
    print(neighborhoods)
    
    isMember = Neighborhood.objects.filter(member = request.user)

    if isMember:
        for hood in isMember:
            hoodName = hood.neighborhoodName
        return redirect(home, hoodName)
    
    form = createJoinHoodForm()
    context = {'form': form, 'neighborhoods': neighborhoods}
    return render(request, 'create_join_hood.html', context)

@login_required(login_url='login')
def createHood(request):
    if request.method == 'POST':
        form = createJoinHoodForm(request.POST)
        if form.is_valid():
            newHood = form.save(commit=False)
            newHood.creator = request.user
            newHood.member = request.user
            newHood.save()
            return redirect(home, hood = newHood.neighborhoodName)
        
        else:
            return redirect(createJoinHood)


@login_required(login_url='login')
def joinHood(request):
    hoodName = request.POST.get('hoodName') 

    try:
        hood = Neighborhood.objects.get(neighborhoodName = hoodName)
        newHood = createJoinHoodForm(instance=hood)
        newHood.member = request.user
        newHood.save()
        return redirect(home, hood= hoodName)
    except:
        messages.error(request, 'An Error Occurred while you were trying to join this neighborhood')
        return redirect(createJoinHood)
