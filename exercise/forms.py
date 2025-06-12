from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    """
    Creates a form for :model:`exercise.Exercise
    """

    class Meta:
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

        model = Exercise
        fields = { "indirectly_targeted_muscles", "recommended_sets", "recommended_reps", "exercise_title", "image", "difficulty", "intensity", "instruction", "equipment", "targeted_muscles", "slug" }


    