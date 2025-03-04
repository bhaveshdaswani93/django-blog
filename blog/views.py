from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import Http404
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import redirect
from .forms import CommentForm

class StartPageListView(ListView):
  template_name = "blog/index.html"
  model = Post
  context_object_name = "posts"

  ordering = ['-date']

  def get_queryset(self):
    queryset = super().get_queryset()
    return queryset[:3]

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
  
class AllPostView(ListView):
  template_name = "blog/all-posts.html"
  model = Post
  context_object_name = "posts"
  ordering = ['-date']
  

def posts(request):
  posts_list = Post.objects.all().order_by("-date")
  return render(request, 'blog/all-posts.html', {
    'posts': posts_list
  })
  
# class SinglePostDetailView(DetailView):
#   template_name = "blog/post-detail.html"
#   model = Post
#   def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_tags'] = self.object.tags.all()
#         context['comment_form'] = CommentForm()
#         return context

class SinglePostDetailView(View):
  def get(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
      'post': post,
      'post_tags': post.tags.all(),
      'comment_form': CommentForm()
    })
  
  def post(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post-detail-page', slug=slug)
    return render(request, 'blog/post-detail.html', {
      'post': post,
      'post_tags': post.tags.all(),
      'comment_form': comment_form
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
