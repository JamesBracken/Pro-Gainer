from django.shortcuts import render

# Create your views here.

def exercise_list(request):
    """
    Renders the exercise list page
    """
    return render(request, "exercise/exercise.html")