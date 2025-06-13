from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """Display the index page."""
    # return render(request, 'home/index.html')
    return redirect('/admin')
