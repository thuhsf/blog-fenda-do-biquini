from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts_oficial/lista_posts.html', {'posts': posts})

def detalhe_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts_oficial/detalhe_posts.html', {'post': post})