from django.contrib import admin
from django.urls import path, re_path
from . import views
from lblog import views as appviews

urlpatterns = [
    path('new', appviews.blog_post_create_view, name="blog_post_create_view"),    
    path('<str:slug>/', appviews.blog_post_detail_view, name='blog_post_detail_view'),
    path('<str:slug>/edit/', appviews.blog_post_update_view, name='blog_post_update_view'),
    path('<str:slug>/delete/', appviews.blog_post_delete_view, name='blog_post_delete_view'),
    path('', appviews.blog_post_list_view, name="blog_post_list_view")
]