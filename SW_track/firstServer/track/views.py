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
            "type" : "buttons",
            "buttons" : ["트랙 조회","전체 트랙 보기"]
        }   
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가

    
    return JsonResponse({ #return 밑에는 공통어
        "message": {
            "text": '학번을 입력해주세요.\nex)17010491'
        },
        'keyboard':{
            'type':'text'
        }
    })