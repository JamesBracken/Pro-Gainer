from django import forms
from .models import Exercise, FavouriteExercises


class ExerciseForm(forms.ModelForm):
    """
    Creates a form for :model:`exercise.Exercise
    """

    class Meta:
        DIFFICULTY_SELECTION = [
            ("easy", "Easy"),
            ("medium", "Medium"),
            ("hard", "Hard"),
        ]
        INTENSITY_SELECTION = [
            ("light", "Light"),
            ("moderate", "Moderate"),
            ("intense", "Intense"),
        ]
        model = Exercise
        fields = (
            "exercise_title",
            "slug",
            "instruction",
            "difficulty",
            "recommended_sets",
            "recommended_reps",
            "intensity",
            "image",
            "targeted_muscles",
            "indirectly_targeted_muscles",
            "equipment",
        )

class AddFavouriteExerciseForm(forms.ModelForm):
    class Meta:
        model = FavouriteExercises
        fields = (
            "exercise_id",
        )