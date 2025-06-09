from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Exercise(models.Model):
    exercise_title = models.CharField(unique=True)
    image = CloudinaryField('image')
    difficulty = models.CharField()
    intensity = models.CharField()
    instruction = models.TextField()
    equipment = models.CharField()
    targeted_muscles = models.CharField()
    indirectly_targeted_muscles = models.CharField()
    slug = models.SlugField()