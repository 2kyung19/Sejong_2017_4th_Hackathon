from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests


def keyboard(request):
    return JsonResponse(
        {
            "type" : "text"
        }   
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가
    
    return JsonResponse({ #return 밑에는 공통어
        "message": {
            "text": '٩(๑`^´๑)۶\n키워드를 넣어서 물어보라냥~!\n\n-키워드-\n*학생회관\n*군자관\n*우정당\nex)학생회관,군자관 목\n\n -키워드-\n*미세먼지\n*날씨\nex)오늘 날씨 어때?,날씨\n\n-키워드-\n*공지사항\n*개발자'
        }
    })