from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    excludes = ['post']
    fields = {
      'user_name': 'Your name',
      'user_email': 'Your email',
      'text': 'Comment'
    }