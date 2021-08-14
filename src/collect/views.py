from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "collect/index.html")


def collect(request):
    result = {"result": False, "message": "致命的なエラー"}
    if request.POST["start_date"] > request.POST["end_date"]:
        result["message"] = "開始日が終了日以降です"
        return JsonResponse(result)

    result["result"] = True
    result["message"] = "OK"
    return JsonResponse(result)
