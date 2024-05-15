from django.db import models
import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('images')
    date = models.DateField(datetime.date.today)