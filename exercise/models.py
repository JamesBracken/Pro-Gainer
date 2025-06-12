from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Exercise(models.Model):
    """
    Stores an exercise item entry
    """
    DIFFICULTY_SELECTION = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    INTENSITY_SELECTION = [
        ('light', 'Light'),
        ('moderate', 'Moderate'),
        ('intense', 'Intense'),
    ]

    exercise_title = models.CharField(unique=True)
    image = CloudinaryField('image')
    difficulty = models.CharField(choices=DIFFICULTY_SELECTION) # select
    intensity = models.CharField(choices=INTENSITY_SELECTION) # select
    instruction = models.TextField(max_length=1000)
    equipment = models.CharField(max_length=300)
    targeted_muscles = models.CharField(max_length=300)
    indirectly_targeted_muscles = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    recommended_sets = models.CharField()
    recommended_reps = models.CharField()

    # This function populates the slug with the slugified title 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.exercise_title))
            return super().save(*args, **kwargs)
        super().save(*args, **kwargs)