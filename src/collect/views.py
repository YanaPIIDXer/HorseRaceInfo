from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .modules.scraping import exec


def index(request):
    return render(request, "collect/index.html")


def collect(request):
    result = {"result": False, "message": "処理に失敗しました"}
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
    if start_date > end_date:
        result["message"] = "開始日が終了日以降です"
        return JsonResponse(result)

    result["result"] = exec(start_date, end_date)
    if result["result"] == True:
        result["message"] = "情報収集が完了しました"
    return JsonResponse(result)
