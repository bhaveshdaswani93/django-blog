from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "date", "author",)
  list_filter = ("author", "tags", "date",)
  prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
  list_display = ("user_name", "post",)
  # list_filter = ("moderated", "date",)
  # search_fields = ("user_name", "user_email", "text",)

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
