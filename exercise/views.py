from django.shortcuts import render
from .models import Exercise

def exercise_list(request):
    """
    Renders the exercise list page
    """
    exercises = Exercise.objects.all()
    return render(request, "exercise/exercise.html", {"exercises": exercises})
