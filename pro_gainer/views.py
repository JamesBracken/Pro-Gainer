from django.shortcuts import render


def index(request):
    """
    Returns the index page

    **Template**
        `index.html`
    """
    return render(request, "index.html")


# Customer error page handlers
# exception parameter is not used in the view however
# this is expected by django
def custom_403(request, exception):
    """
    Handles 403 errors by rendering the 403.html template

    **Template**
        `403.html`
    """
    return render(request, "403.html", status=403)


# exception parameter is not used in the view however
# this is expected by django
def custom_404(request, exception):
    """
    Handles 404 errors by rendering the 404.html template

    **Template**
        `404.html`
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Handles 500 errors by rendering the 500.html template

    **Template**
        `500.html`
    """
    return render(request, "500.html", status=500)
