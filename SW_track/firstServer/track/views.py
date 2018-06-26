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

    if return_str=='트랙 조회':
        return JsonResponse({
            "message": {
                "text": '학번을 입력해주세요.\nex)17010491'
            },
            "keyboard":{
                "type":"text"
            }
        })

    elif return_str=="전체 트랙 보기":
        return JsonResponse({
            "message": {
                "text": '트랙을 선택하세요'
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방"]
            }
        })


def track_all(track):
    req = urllib.request.Request("http://interface518.dothome.co.kr/track.html", headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    text = response.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    tname = soup.find_all('td',{'class':'tname'})
    tbase = soup.find_all('td',{'class':'tbase'})
    tuse = soup.find_all('td',{'class':'tuse'})

    all = [0,0,0,0,0,0,0,0,0,0]

    for n in tname:
        i = tname.index(n)
        tname[i]= n.get_text()
        
    for n in tbase:
        i = tbase.index(n)
        tbase[i]= n.get_text()

    for n in tuse:
        i = tuse.index(n)
        tuse[i]= n.get_text()


    for i in range(0,len(tname)):
        all[i] = str(i+1)+ '.' + str(tname[i]) + '\n\n*기초교과*\n' + str(tbase[i]) + '\n\n*응용교과*\n' + str(tuse[i])

        
    list=all[track].split(",")

    abc=""
    for i in range(0,len(list)):
        abc=abc+list[i]+"\n"

    return abc

    

def id(usernumber):
    req = urllib.request.Request("http://interface518.dothome.co.kr/track.html", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")
    soup = BeautifulSoup(text, 'html.parser')

    sjnumber=soup.find_all("td",{'class',"number"})
    sjname=soup.find_all("td",{'class',"name"})
    sjtrack=soup.find_all("td",{'class',"track"})
    
    for n in sjname:
        i = sjname.index(n)
        sjname[i]= n.get_text()

    for n in sjnumber:
        i = sjnumber.index(n)
        sjnumber[i]= n.get_text()
        sjnumber[i]=int(sjnumber[i])
        
    for n in sjtrack:
        i = sjtrack.index(n)
        sjtrack[i]= n.get_text()

    for i in range(0,len(sjnumber)):
        if sjnumber[i]==usernumber: #입력한 학번에 대한 정보를 알기 위해
            index1=i
            break

    username=sjname[index1]
    usertrack=sjtrack[index1]

    printstr=username+" 님은 "+usertrack+"트랙 과정 중입니다."
    return printstr