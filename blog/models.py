from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="image/")
    text_body = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text_body[:100]

    def pretty_time(self):
        return self.pub_date.strftime('%b %e %Y')