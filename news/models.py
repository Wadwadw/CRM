from django.db import models
from leads.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    body_news = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


