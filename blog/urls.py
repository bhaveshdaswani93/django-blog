from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='starting-page'),
  path('', views.StartPageListView.as_view(), name='starting-page'),
  path('posts', views.posts, name='post-list'),
  path('posts/<slug:slug>', views.post_detail, name='post-detail-page')
]