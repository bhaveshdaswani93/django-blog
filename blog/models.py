from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
  first_name: models.CharField(max_length=100)
  last_name: models.CharField(max_length=100)
  email: models.EmailField()

# Create your models here.
class Post(models.Model):
  title: models.CharField(max_length=150)
  excerpt: models.CharField(max_length=200)
  image: models.CharField(max_length=200)
  date: models.DateField(auto_now=True)
  content: models.TextField(validators=[MinLengthValidator(100)])
  slug: models.SlugField(unique=True, db_index=True)
  author: models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='books')
  