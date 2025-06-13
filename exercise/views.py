from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise
from .forms import ExerciseForm
from django.contrib.admin.views.decorators import staff_member_required


def exercise_list(request):
    """
    Renders the exercise list page
    """
    exercises = Exercise.objects.all()
    return render(request, "exercise/exercise_list.html", {"exercises": exercises})


def exercise_detail(request, exercise_slug):
    """
    Renders the exercise list page
    """
    exercise = get_object_or_404(Exercise, slug=exercise_slug)

    return render(request, "exercise/exercise_detail.html", {"exercise": exercise})


@staff_member_required
def add_exercise_item(request):

    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, request.FILES)
        if exercise_form.is_valid():
            exercise_form.save()
        return redirect("exercise_list")
    else:
        exercise_form = ExerciseForm()
        return render(request, "exercise/exercise_form.html", {"exercise_form": exercise_form,})
