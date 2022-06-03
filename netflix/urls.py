from django.urls import path
from .views import home,CustomLoginView, profile,register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('home/',home,name='home'),
    path('movie/<int:movie_id>',views.movie_details,name='details'),
    path('',views.landing,name='landing'),

    # user to be moved to a new app
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name = 'register'),
    path('logout/',LogoutView.as_view(template_name = 'netflix/logout.html'),name='logout'),
    path('account/<int:user_id>',views.profile,name='profile')
]