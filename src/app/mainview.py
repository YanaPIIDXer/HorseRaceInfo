from django.http import HttpResponse
from django.shortcuts import render

from collect.models import CourseInfo


def index(request):
    return render(request, "main/index.html")
