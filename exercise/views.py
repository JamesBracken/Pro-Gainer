from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise
from .forms import ExerciseForm
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator


def exercise_list(request):
    """
    Renders the exercise list page

    **Context**

    ``page_obj``
        List of up to 30 instances of :model:`exercise.Exercise`

    **Template**

    ``exercise/exercise_list.html``
    """
    exercise_list = Exercise.objects.all()
    # The pagination here was made with assistance from the django pagination docs
    # https://docs.djangoproject.com/en/5.2/topics/pagination/

    # Paginator controls will display 30 exercises from the list per page
    paginator = Paginator(exercise_list, 30)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "exercise/exercise_list.html", {"page_obj": page_obj})


def exercise_detail(request, exercise_slug):
    """
    Renders the exercise detail page

    **Context**

    ``exercise``
        Instance of :model:`exercise.Exercise`

    **Template**

    ``exercise/exercise_detail.html``
    
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
        return render(
            request,
            "exercise/exercise_form.html",
            {
                "exercise_form": exercise_form,
            },
        )


@staff_member_required
def edit_exercise_item(request, exercise_slug):
    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()
        # Later this will be adjusted to return the user to
        # The same page of the exercise which has been edited
        return redirect("exercise_detail", exercise_slug=exercise.slug)
    else:
        exercise_form = ExerciseForm(instance=exercise)
        template = "exercise/exercise_form.html"
        context = {
            "exercise_form": exercise_form,
        }
        return render(request, template, context)


@staff_member_required
def delete_exercise_item(request, exercise_slug):
    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    exercise.delete()
    return redirect("exercise_list")