from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "collect/index.html")


def collect(request):
    return JsonResponse({"result": "OK"})
