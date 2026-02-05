from django.urls import path
from . import views

urlpatterns=[
    path('posts/',views.posts,name='posts'),
    path('post/<int:pk>',views.post,name='post')
] 