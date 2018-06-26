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

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['트랙조회', '1', '아리수', '기숙사식당', '교직원식당']
    })


@csrf_exempt
def message(request) :
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
 
    requestMode = return_str.encode('utf-8') # utf-8형식으로 인코딩하여 한글을 인식
     
    if requestMode == '트랙조회' :
        return JsonResponse({
             'message' : {
                 'text' : "번역할 내용을 다음과 같이 입력해 주세요.(개발중)\n ex)번역 뭐해?, 번역 안녕ㅋㅋ\n 형식을 갖추지 않으면 답변이 나오지 않습니다ㅜㅜ."
             },
             'keyboard' : {
                 'type' : 'text' # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
             }
        })