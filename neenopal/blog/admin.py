from csv import list_dialects
from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'createdDate', 'author', 'description', 'isPublished']