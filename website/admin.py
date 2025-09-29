from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['id' , 'title']
    list_display = ['id' , 'title' , 'content' , 'created_at']
    list_display_links = ['id' , 'title']
    list_filter = ['created_at']
    search_fields = ['title']
    