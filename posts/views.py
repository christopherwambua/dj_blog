from django.shortcuts import render
from .models import Posts   

# Create your views here.

def posts(request):
    post= Posts.objects.all()
    context={'post':post}
    return render(request,'post_list.html',context) 