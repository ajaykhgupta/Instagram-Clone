
# app URLs FILE

from django.contrib import admin
from django.urls import path
from Instagram import views

urlpatterns = [
    path('', views.view_login, name="login" ),
    # path('', views.index, name="home" ),
    path('explore', views.explore, name="explore" ),
    path('signup', views.signup, name="signup" ),
    path('inbox', views.inbox, name="inbox" ),
    path('profile', views.profile, name="profile" ),
    path('signup', views.signup, name="signup" ),
    path('login', views.view_login, name="login" ),
]



