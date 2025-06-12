from django.shortcuts import render, get_object_or_404
from .models import Exercise

def exercise_list(request):
    """
    Renders the exercise list page
    """
    exercises = Exercise.objects.all()
    return render(request, "exercise/exercise.html", {"exercises": exercises})

def exercise_detail(request, exercise_slug):
    """
    Renders the exercise list page
    """
    exercise = get_object_or_404(Exercise, slug=exercise_slug)

    return render(request, "exercise/exercise_detail.html", {"exercise": exercise})
