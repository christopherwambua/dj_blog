from django.shortcuts import render
from .models import Posts   

# Create your views here.

def posts(request):
    post= Posts.objects.all()
    context={'post':post}
    return render(request,'post_list.html',context) 

def post(request,pk=None):
    if pk:
        post_item=Posts.objects.get(pk=pk)
    else:
        post_item=""

    context={'post':post_item}

    return render(request,'post.html',context)