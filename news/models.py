from django.db import models
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    create = models.DateTimeField(default=datetime.datetime.now, blank=True)
    img_url = models.URLField()
    



    def __str__(self):
        return self.title
        
