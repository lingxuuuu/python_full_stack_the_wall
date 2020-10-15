from django.urls import path     
from . import views

urlpatterns = [
    #display
    path('', views.index),
    path('wall', views.wall),	   

    #redirect
    path('process_register', views.register),
    path('process_login', views.login),
    path('add_post', views.add_post),
    path('logout', views.logout),
    path('post_comment/<int:post_id>', views.comment),
   ]