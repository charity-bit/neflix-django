from django import dispatch
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

import random

import requests

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from netflix.models import User, Profile
from django.views.decorators.csrf import csrf_exempt,csrf_protect


from .forms import NewUserForm,GetStartedForm



def get_trailer(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=9bee7f4337138daebd214178b06dcc51&language=en').json()['results']
    key = None

    if response:
        for item in response:
            if item.get('type') == 'Trailer':
                key = item.get('key')

    return key



def get_movies(category):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{category}?api_key=9bee7f4337138daebd214178b06dcc51&language=en-US&page=1').json()['results']
    movies = []
    if response:
        for item in response:
            if (item.get('title') or item.get('name')) and item.get('overview') and (item.get('poster_path') or item.get('backdrop_path')):
                movies.append(item)

    return movies

def get_neflix_originals():
    response = requests.get('https://api.themoviedb.org/3/discover/tv?api_key=9bee7f4337138daebd214178b06dcc51&with_networks=213').json()['results']
    movies = []
    if response:
        for item in response:
            if (item.get('title') or item.get('name')) and item.get('overview') and (item.get('poster_path') or item.get('backdrop_path')):
                movies.append(item)

    return movies

                
@login_required(login_url='/')
def home(request):
    
    movie = random.choice(get_movies('now_playing'))
    key = get_trailer(movie.get('id'))

    # categories

    # now playing
    now_playing = get_neflix_originals()
    # popular
    popular = get_movies('popular')
    # genres

    context = {
        'movie':movie,
        'key':key,
        'popular':popular,
        'now_playing':now_playing
    }
    return render(request,'netflix/home.html',context)


@method_decorator(csrf_exempt,name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'netflix/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
        
    else: 

        form = NewUserForm()

    context = {
        'form':form
        }

    return render(request,'netflix/register.html',context)


@login_required(login_url='/')
def profile(request,user_id):

    try:
        user = User.objects.get(id = user_id)
        profiles = Profile.objects.filter(user_id = user_id)
        length = len(profiles)
        # profiles = request.user.profiles.all()
    
    except  Profile.DoesNotExist or User.DoesNotExist:
        return redirect('home')
    context = {
        'profiles': profiles,
        'length':length
    }
    return render(request,'netflix/profile.html',context)




@login_required(login_url='/')
def movie_details(request,movie_id):
    return render(request,'netflix/details.html')

@csrf_exempt
def landing(request):
    if request.method == 'POST':
        form = GetStartedForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email = email)
            if user:
                return redirect('login')

            else:
                return redirect('register')
          
    else:
        form = GetStartedForm()
    context = {
        'form':form
    }
    return render(request,'netflix/landingpage.html',context)
