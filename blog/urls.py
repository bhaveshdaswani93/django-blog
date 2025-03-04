from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='starting-page'),
  path('', views.StartPageListView.as_view(), name='starting-page'),
  path('posts', views.AllPostView.as_view(), name='post-list'),
  path('posts/<slug:slug>', views.SinglePostDetailView.as_view(), name='post-detail-page')
]