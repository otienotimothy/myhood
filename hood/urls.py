from django.urls import path

from .views import index, signupUser, loginUser, createJoinHood

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('create-join-hood/', createJoinHood, name='create-join-hood')
]