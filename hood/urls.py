from django.urls import path

from .views import index, home, signupUser, loginUser, logoutUser, createJoinHood, createHood, joinHood, service, business

urlpatterns = [
    path('', index, name='index'),
    path('hood/<str:hood>/', home, name='home' ),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('create-join-hood/', createJoinHood, name='create-join-hood'),
    path('create-hood/', createHood, name='create-hood' ),
    path('join-hood/', joinHood, name='join-hood' ),
    path('service/<str:hood>/', service, name='service'),
    path('business/<str:hood>/', business, name='business'),
]