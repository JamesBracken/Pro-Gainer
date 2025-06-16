from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise, FavouriteExercises
from .forms import ExerciseForm, AddFavouriteExerciseForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


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
    # Passing in this boolean for javascript to conditionally add styles
    is_exercise_favourite = FavouriteExercises.objects.filter(
        user=request.user, exercise_id=exercise.id
    ).exists()

    toggle_exercise_form = AddFavouriteExerciseForm(
        initial={
            "exercise_id": exercise,
        }
    )
    context = {
        "exercise": exercise,
        "toggle_exercise_form": toggle_exercise_form,
        "is_exercise_favourite": is_exercise_favourite,
    }
    return render(request, "exercise/exercise_detail.html", context)


@staff_member_required
def add_exercise_item(request):
    """
    Displays a form for admins to create a new instance of :model:`exercise.Exercise`

    **Context**

    ``exercise_form``
        An instance of :form:`exercise.ExerciseForm`

    **Template**

    `exercise/exercise_form.html
    """
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, request.FILES)
        if exercise_form.is_valid():
            exercise_form.save()
            messages.add_message(request, messages.SUCCESS, "Exercise has been added")
        else:
            messages.add_message(request, messages.ERROR, "Error adding exercise")
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
    """
    Displays a form for admins to edit an existing instance of :model:`exercise.Exercise`

    **Context**

    ``exercise``
        The selected instance of :model:`exercise.Exercise`
    ``exercise_form``
        An instance of :form:`exercise.ExerciseForm`

    **Template**

    `exercise/exercise_form.html
    """
    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()
            messages.add_message(request, messages.SUCCESS, "Exercise has been edited")
        else:
            messages.add_message(request, messages.ERROR, "Error editing exercise")
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
    """
    Deletes an instance of :model:`exercise.Exercise`

    **Context**

    ``exercise``
        An instance of :model:`exercise.Exercise
    """

    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    exercise.delete()
    messages.add_message(request, messages.SUCCESS, "Exercise has been deleted")
    return redirect("exercise_list")


@login_required
def favourite_exercise_list(request):
    favourite_exercises = FavouriteExercises.objects.filter(user=request.user)
    context = {
        "exercises": favourite_exercises,
    }
    return render(request, "exercise/favourite_exercises_list.html", context)


@login_required
def toggle_is_favourite_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    exercise_slug = exercise.slug
    is_exercise_favourite = FavouriteExercises.objects.filter(
        user=request.user, exercise_id=exercise_id
    ).exists()

    if request.method == "POST":
        toggle_exercise_form = AddFavouriteExerciseForm(request.POST)
        if is_exercise_favourite:
            favourite_exercise = FavouriteExercises.objects.filter(
                user=request.user, exercise_id=exercise_id
            )
            favourite_exercise.delete()

            return redirect("exercise_detail", exercise_slug)
        if toggle_exercise_form.is_valid():
            favourite_exercise = toggle_exercise_form.save(commit=False)
            favourite_exercise.user = request.user
            toggle_exercise_form.save()
            return redirect("exercise_detail", exercise_slug)
