from django.http import JsonResponse
from django.shortcuts import render
from .modules.scraping import exec


def index(request):
    return render(request, "collect/index.html")


def collect(request):
    result = {"result": False, "message": "処理に失敗しました"}

    result["result"] = exec()
    if result["result"] == True:
        result["message"] = "情報収集が完了しました"
    return JsonResponse(result)
