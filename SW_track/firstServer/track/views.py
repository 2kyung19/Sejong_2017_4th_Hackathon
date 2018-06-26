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

    #################################################################트랙조회
    if return_str=='트랙 조회':
        return JsonResponse({
            "message": {
                "text": '학번을 입력해주세요.\nex)17010491'
            },
            "keyboard":{
                "type":"text"
            }
        })

    elif return_str.find("1")!=-1:

        userid=int(return_str)
        return JsonResponse({
            "message":{
                "text":id(int(return_str))+"\n조회 하실 교과목을 선택하세요."
            },
            "keyboard":{
                "type":"buttons",
                "buttons":["트랙 기초교과","트랙 응용교과","처음으로"]
            }
        })

    elif return_str=="트랙 기초교과":
        return JsonResponse({
            "message":{
                "text":tbase(userid)
            }
        })

    elif return_str=="트랙 응용교과":
        return JsonResponse({
            "message":{
                "text":tuse(userid)
            }
    })    
    
    #################################################################전체트랙보기

    elif return_str=="전체 트랙 보기":
        return JsonResponse({
            "message": {
                "text": '트랙을 선택하세요'
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })

    elif return_str=="HCI & 비쥬얼컴퓨팅":
        return JsonResponse({
            "message": {
                "text": all_track(0)
            }
        })    

    elif return_str=="멀티미디어":
        return JsonResponse({
            "message": {
                "text": all_track(1)
            }
        })
    elif return_str=="사물인터넷":
        return JsonResponse({
            "message": {
                "text": all_track(2)
            }
        })
    
    elif return_str=="시스템응용":
        return JsonResponse({
            "message": {
                "text": all_track(3)
            }
        })

    elif return_str=="인공지능":
        return JsonResponse({
            "message": {
                "text": all_track(4)
            }
        })
    elif return_str=="가상현실":
        return JsonResponse({
            "message": {
                "text": all_track(5)
            }
        })
    
    elif return_str=="정보보호":
        return JsonResponse({
            "message": {
                "text": all_track(6)
            }
        })
    
    elif return_str=="데이터사이언스":
        return JsonResponse({
            "message": {
                "text": all_track(7)
            }
        })
    
    elif return_str=="SW교육":
        return JsonResponse({
            "message": {
                "text": all_track(8)
            }
        })
    
    elif return_str=="사이버국방":
        return JsonResponse({
            "message": {
                "text": all_track(9)
            }
        })
    
    else: #처음으로
        return JsonResponse({
            "keyboard":{
                "type":"buttons",
                "buttons" : ["트랙 조회","전체 트랙 보기"]
            }
        })

####################################################################################################

def all_track(track):
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