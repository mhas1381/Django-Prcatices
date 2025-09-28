from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    
    return render(request , 'index.html' , context )

def single_post(request , id):
    post = get_object_or_404(Post , id = id)
    
    return render(request , 'post.html' , {'post':post})

    
