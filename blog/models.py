from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="image/")
    text_body = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
