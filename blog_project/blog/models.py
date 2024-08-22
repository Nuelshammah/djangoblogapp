from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class post(models. Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
         on_delete=models.CASCADE
         )
    body = models.TextField()

    def __str__(self):
        return str(self.title)  

    def get_absolute_url(self):
        return reverse('home')    

class comment(models.Model):
    post = models.ForeignKey(post, on_delete= models.CASCADE, related_name= 'comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    Created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"Comment by {self.author} on {self.post}"        