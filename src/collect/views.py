from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "collect/index.html")


def collect(request):
    return redirect("/")
