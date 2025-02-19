from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import Http404
from .models import Post

# Create your views here.
def get_sort_key(post):
  return post['date']

def index(request):
  #print(posts_list)
  latest_posts = Post.objects.all().order_by('-date')[:3]
  #latest_posts = sorted(posts_list, key=get_sort_key, reverse=True)
  #latest_posts = list(latest_posts[:3])

  return render(request, 'blog/index.html', {
    'posts': latest_posts
  })

def posts(request):
  posts_list = Post.objects.all().order_by("-date")
  return render(request, 'blog/all-posts.html', {
    'posts': posts_list
  })

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  
  return render(request, 'blog/post-detail.html', {
      'post': post,
      'post_tags': post.tags.all()
    })
  #try: 
    #print(list(post for post in posts_list if post['slug'] == slug))
   # post = next(post for post in posts_list if post['slug'] == slug)
   
  # post = Post.objects.get(slug=slug)
  
  #except:
    #raise Http404()
