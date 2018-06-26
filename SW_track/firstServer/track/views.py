from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests

userid=0

def keyboard(request):
    return JsonResponse(
        {
            "type" : "buttons",
            "buttons" : ["자신의 트랙 조회","전체 트랙 보기","소프트웨어융합대학 사이트"]
        }   
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가

    #################################################################트랙조회
    if return_str=='자신의 트랙 조회':
        return JsonResponse({
            "message": {
                "text": '학번을 입력해주세요.\nex)17010491'
            },
            "keyboard":{
                "type":"text"
            }
        })

    elif return_str.find("1")!=-1:
        global userid
        userid=int(return_str)
        
        if idCheck(userid)==True:
            return JsonResponse({
                "message":{
                    "text":id(userid,1)+"\n조회 하실 교과목을 선택하세요."
                },
                "keyboard":{
                    "type":"buttons",
                    "buttons":["트랙 기초교과","트랙 응용교과","처음으로"]
                }
            })

        elif idCheck(userid)==False:
            return JsonResponse({
                "message":{
                    "text":"다시 시도하세요."
                },
                "keyboard":{
                    "type":"buttons",
                    "buttons" : ["자신의 트랙 조회","전체 트랙 보기","소프트웨어융합대학 사이트"]
                }
        })             

    elif return_str=="트랙 기초교과":
        return JsonResponse({
            "message":{
                "text":id(userid,2)
            },
            "keyboard":{
                "type":"buttons",
                "buttons":["트랙 기초교과","트랙 응용교과","처음으로"]
            }
        })

    elif return_str=="트랙 응용교과":
        return JsonResponse({
            "message":{
                "text":id(userid,3)
            },
            "keyboard":{
                "type":"buttons",
                "buttons":["트랙 기초교과","트랙 응용교과","처음으로"]
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
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })    

    elif return_str=="멀티미디어":
        return JsonResponse({
            "message": {
                "text": all_track(1)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    elif return_str=="사물인터넷":
        return JsonResponse({
            "message": {
                "text": all_track(2)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    
    elif return_str=="시스템응용":
        return JsonResponse({
            "message": {
                "text": all_track(3)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })

    elif return_str=="인공지능":
        return JsonResponse({
            "message": {
                "text": all_track(4)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    elif return_str=="가상현실":
        return JsonResponse({
            "message": {
                "text": all_track(5)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    
    elif return_str=="정보보호":
        return JsonResponse({
            "message": {
                "text": all_track(6)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    
    elif return_str=="데이터사이언스":
        return JsonResponse({
            "message": {
                "text": all_track(7)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    
    elif return_str=="SW교육":
        return JsonResponse({
            "message": {
                "text": all_track(8)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    
    elif return_str=="사이버국방":
        return JsonResponse({
            "message": {
                "text": all_track(9)
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["HCI & 비쥬얼컴퓨팅","멀티미디어","사물인터넷","시스템응용","인공지능","가상현실","정보보호","데이터사이언스","SW교육","사이버국방","처음으로"]
            }
        })
    

    elif return_str=="처음으로":
        return JsonResponse({
            "message":{
                "text":"버튼을 선택하세요."
            },
            "keyboard":{
                "type":"buttons",
                "buttons" : ["자신의 트랙 조회","전체 트랙 보기","소프트웨어융합대학 사이트"]
            }
        })

    elif return_str=="소프트웨어융합대학 사이트":
         return JsonResponse({
                "message":{
                    "text":"소프트웨어 융합대학 홈페이지",
                    "message_button": {
                        "label": "홈페이지 바로가기",
                        "url": "http://www.sejong.ac.kr/college/software.html?menu_id=1.12"
                    }
                },
                "keyboard":{
                    "type":"buttons",
                    "buttons" : ["자신의 트랙 조회","전체 트랙 보기","소프트웨어융합대학 사이트"]
                }
            })

    else:
        return JsonResponse({
            "message":{
                "text":"다시 시도하세요."
            },
            "keyboard":{
                "type":"buttons",
                "buttons" : ["자신의 트랙 조회","전체 트랙 보기","소프트웨어융합대학 사이트"]
            }
        })

####################################################################################################

def all_track(track):
    req = urllib.request.Request("http://interface518.dothome.co.kr/track/track.html", headers={'User-Agent': 'Mozilla/5.0'})
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

#해당 id가 데이터에 있느냐 없느냐
def idCheck(usernumber):
    req = urllib.request.Request("http://interface518.dothome.co.kr/track/student.html", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")
    soup = BeautifulSoup(text, 'html.parser')

    sjnumber=soup.find_all("td",{'class',"number"})
    for n in sjnumber:
        i = sjnumber.index(n)
        sjnumber[i]= n.get_text()
        sjnumber[i]=int(sjnumber[i])
    
    cnt=False
    #입력한 학번에 대한 정보를 알기 위해
    for i in range(0,len(sjnumber)):
        if sjnumber[i]==id:
            cnt=True
            break
    return cnt

def id(usernumber,num):
    req = urllib.request.Request("http://interface518.dothome.co.kr/track/student.html", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")
    soup = BeautifulSoup(text, 'html.parser')

    ##문자 파싱 >>목록 추가
    sjnumber=soup.find_all("td",{'class',"number"})
    sjname=soup.find_all("td",{'class',"name"})
    sjtrack=soup.find_all("td",{'class',"track"})
    sjtrackbase=soup.find_all("td",{'class',"trackbase"})
    sjtrackuse=soup.find_all("td",{'class',"trackuse"})

    ##쓰레기값 제거
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

    for n in sjtrackbase:
        i = sjtrackbase.index(n)
        sjtrackbase[i]= n.get_text()

    for n in sjtrackuse:
        i = sjtrackuse.index(n)
        sjtrackuse[i]= n.get_text()

    #입력한 학번에 대한 정보를 알기 위해 인덱스 추출
    for i in range(0,len(sjnumber)):
        if sjnumber[i]==usernumber:
            index1=i #index1=> 이름/학번/선택한 트랙
            break

    username=sjname[index1]
    usertrack=[]
    if sjtrack[index1].find(",")!=-1:
        usertrack=sjtrack[index1].split(",")

    else:
        usertrack.append(sjtrack[index1])

    if num==1:
        printstr=username+" 님은 \n"
        for i in range(0,len(usertrack)):
            printstr=printstr+usertrack[i]+'\n'
        printstr+="트랙 과정 중입니다.\n"
        return printstr