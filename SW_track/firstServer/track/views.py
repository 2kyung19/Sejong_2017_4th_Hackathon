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
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    return JsonResponse({
            'message': {
                    'text': "button test : " + return_str
            },
            'keyboard': {
                    'type': 'buttons',
                    'buttons': ['1','2']
            }
    })