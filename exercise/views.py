from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Exercise, FavouriteExercise
from .forms import ExerciseForm, AddFavouriteExerciseForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST
from membership.utils import is_user_membership_active



def exercise_list(request):
    """
    Renders the exercise list page

    **Context**

    ``page_obj``
        List of up to 30 instances of :model:`exercise.Exercise`

    **Template**

    ``exercise/exercise_list.html``
    """
    exercise_list = Exercise.objects.all().order_by("-created_at")
    # The pagination here was made with assistance from the django pagination
    # docs
    # https://docs.djangoproject.com/en/5.2/topics/pagination/

    # Paginator controls will display 30 exercises from the list per page
    paginator = Paginator(exercise_list, 30)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "exercise/exercise_list.html", {"page_obj": page_obj}
    )


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
    is_exercise_favourite = False
    toggle_exercise_form = AddFavouriteExerciseForm(
        initial={
            "exercise": exercise,
        }
    )
    if (request.user.is_authenticated and
            is_user_membership_active(request.user)):
        is_exercise_favourite = FavouriteExercise.objects.filter(
            user=request.user, exercise=exercise.id
        ).exists()
        context = {
            "exercise": exercise,
            "toggle_exercise_form": toggle_exercise_form,
            "is_exercise_favourite": is_exercise_favourite,
        }
    else:
        context = {
            "exercise": exercise,
            "toggle_exercise_form": toggle_exercise_form,
        }

    return render(request, "exercise/exercise_detail.html", context)


@staff_member_required
def add_exercise_item(request):
    """
    Displays a form for admins to create a new instance of
    :model:`exercise.Exercise`

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
            messages.add_message(
                request, messages.SUCCESS, "Exercise has been added"
            )
            return redirect("exercise_list")
        else:
            return render(
                request,
                "exercise/exercise_form.html",
                {
                    "exercise_form": exercise_form,
                },
            )
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
    Displays a form for admins to edit an existing instance of
    :model:`exercise.Exercise`

    **Context**

    ``exercise``
        The selected instance of :model:`exercise.Exercise`

    ``exercise_form``
        An instance of :form:`exercise.ExerciseForm`

    **Template**

    `exercise/exercise_form.html`
    """
    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    if request.method == "POST":
        exercise_form = ExerciseForm(
            request.POST, request.FILES, instance=exercise
        )
        if exercise_form.is_valid():
            exercise_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"{ exercise.exercise_title } has been edited",
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                f"Error editing { exercise.exercise_title }"
            )
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

    ``exercise.Exercise``
        An instance of :model:`exercise.Exercise
    """
    exercise = get_object_or_404(Exercise, slug=exercise_slug)
    exercise.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        f"{ exercise.exercise_title } has been deleted"
    )
    return redirect("exercise_list")


@login_required
def favourite_exercise_list(request):
    """
    Displays a list of instances of :model:`exercise.FavouriteExercise`

    **Context**

    ``favourite_exercises``
        An instance of :model:`exercise.FavouriteExercise
    """
    if is_user_membership_active(request.user):
        favourite_exercises = FavouriteExercise.objects.filter(
            user=request.user
        ).order_by("-added_at")
        paginator = Paginator(favourite_exercises, 30)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)
        context = {
            "page_object": page_object,
        }
        return render(
            request, "exercise/favourite_exercises_list.html", context
        )
    messages.add_message(
        request,
        messages.ERROR,
        "You must have an active membership to access favourites",
    )
    return redirect(reverse("home"))

@require_POST
@login_required
def toggle_is_favourite_exercise(request, exercise_id):
    """
    Toggles exercises to be added or deleted as an instance of
    :model:`FavouriteExercise`

    **Context**

    ``toggle_exercise_form``
        An instance of :form:`exercise.AddFavouriteExerciseForm`

    ``favourite_exercise``
        An instance of :model:`exercise.FavouriteExercise`
    """
    if is_user_membership_active(request.user):
        exercise = get_object_or_404(Exercise, id=exercise_id)
        exercise_slug = exercise.slug
        is_exercise_favourite = FavouriteExercise.objects.filter(
            user=request.user, exercise=exercise_id
        ).exists()

        toggle_exercise_form = AddFavouriteExerciseForm(request.POST)
        if is_exercise_favourite:
            favourite_exercise = FavouriteExercise.objects.filter(
                user=request.user, exercise=exercise_id
            )
            favourite_exercise.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"{ exercise.exercise_title } has been removed to your "
                f"favourites list",
            )
            return redirect("exercise_detail", exercise_slug)
        if toggle_exercise_form.is_valid():
            favourite_exercise = toggle_exercise_form.save(commit=False)
            favourite_exercise.user = request.user
            toggle_exercise_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"{ exercise.exercise_title } has been added to your "
                f"favourites list",
            )
            return redirect("exercise_detail", exercise_slug)
    messages.add_message(
        request,
        messages.SUCCESS,
        "You must have an active membership to access favourites",
    )
    return redirect(reverse("home"))
