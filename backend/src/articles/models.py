from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Article(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title