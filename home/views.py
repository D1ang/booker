from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse


def index(_request: HttpRequest) -> HttpResponse:
    """Display the index page."""
    return redirect('/admin')
