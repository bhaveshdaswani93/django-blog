from django.shortcuts import render
from datetime import date

posts = [
  {
    'slug': 'hike-in-the-mountains',
    'image': 'mountains.jpg',
    'author': 'Yan',
    'date': date(2021, 8, 12),
    'title': 'Mountain Hiking',
    'excerpt': 'There\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened on this hike.',
    'content': """
          lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Sed ut ultricies risus. Nullam eget libero at nunc
          maximus dictum. Nullam porttitor, eros nec tristique
          fermentum, ligula libero suscipit magna, nec pulvinar
        """

  }
]

# Create your views here.
def get_sort_key(post):
  return post['date']

def index(request):
  latest_posts = sorted(posts, key=get_sort_key, reverse=True)
  latest_posts = list(posts[:3])

  return render(request, 'blog/index.html', {
    'posts': latest_posts
  })

def posts(request):
  return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
  return render(request, 'blog/post-detail.html')
