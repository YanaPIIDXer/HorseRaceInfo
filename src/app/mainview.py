from django.http import HttpResponse
from django.shortcuts import render

from collect.models import CourseInfo


def index(request):
    coursers = CourseInfo.objects.all().order_by("id")
    params = {
        'courses': coursers
    }
    return render(request, "main/index.html", params)
