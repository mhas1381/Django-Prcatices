from django.db import models

def post_directory_path(instance , filename):
    # file will be uploaded to MEDIA_ROOT/post_<id>/<filename>
    return f"post_{instance}/{filename}"
    
    
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to=post_directory_path)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title