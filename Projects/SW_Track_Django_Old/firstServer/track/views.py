from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
from .models import Track
from .models import Student
import requests

userid=0
tuse=[]
tbase=[]
tname=[]

def index(request):
    candidates = Track.objects.all()
    context = {'candidates' : candidates} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'track/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달

def index1(request):
    candidates = Student.objects.all()
    context = {'candidates' : candidates} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'student/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달

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
        
        ########데이터에 있는 학번########
        if idCheck(int(return_str))==True:
            global userid
            userid=int(return_str)

            return JsonResponse({
                "message":{
                    "text":id(userid,1)+"\n조회 하실 교과목을 선택하세요."
                },
                "keyboard":{
                    "type":"buttons",
                    "buttons":["트랙 기초교과","트랙 응용교과","자세히보기","처음으로"]
                }
            })

        #######데이터에 없는 학번#########
        elif idCheck(int(return_str))==False:
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
                "buttons":["트랙 기초교과","트랙 응용교과","자세히보기","처음으로"]
            }
        })

    elif return_str=="트랙 응용교과":
        return JsonResponse({
            "message":{
                "text":id(userid,3)
            },
            "keyboard":{
                "type":"buttons",
                "buttons":["트랙 기초교과","트랙 응용교과","자세히보기","처음으로"]
            }
    })

    elif return_str=="자세히보기":
        return JsonResponse({
            "message":{
                    "text":"트랙 이수 상황에 대해 더 알아보고 싶다면?",
                    "message_button": {
                        "label": "이수 현황 조회하기",
                        "url": id(userid,4)
                    }
                },
                "keyboard":{
                    "type":"buttons",
                    "buttons":["트랙 기초교과","트랙 응용교과","자세히보기","처음으로"]
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
    
    #############################################################기타 버튼
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

    #######################################################오류
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

################################################함수####################################################

##전체 트랙을 읽어서 목록 값에 저장##
def trackread():
    global tname
    global tbase
    global tuse

    treq = urllib.request.Request("http://ec2-18-216-35-115.us-east-2.compute.amazonaws.com:8000/track", headers={'User-Agent': 'Mozilla/5.0'})
    tresponse = urllib.request.urlopen(treq)
    ttext = tresponse.read().decode("utf8")
    tsoup = BeautifulSoup(ttext, 'html.parser')

    tname = tsoup.find_all('td',{'class':'tname'})
    tbase = tsoup.find_all('td',{'class':'tbase'})
    tuse = tsoup.find_all('td',{'class':'tuse'})

    for n in tname:
        i = tname.index(n)
        tname[i]= n.get_text().replace(" ","")
        
    for n in tbase:
        i = tbase.index(n)
        tbase[i]= n.get_text().replace(" ","")

    for n in tuse:
        i = tuse.index(n)
        tuse[i]= n.get_text().replace(" ","")

##전체 트랙값 스트링 반환 함수##
def all_track(track):
    global tnum
    global tuse
    global tbase

    trackread()

    all = [0,0,0,0,0,0,0,0,0,0]

    #all에다가 문자열을 추가
    for i in range(0,len(tname)):
        all[i] = str(i+1)+ '.' + str(tname[i]) + '\n\n*기초교과*\n' + str(tbase[i]) + '\n\n*응용교과*\n' + str(tuse[i])
        
    list=all[track].split(",")

    abc=""
    for i in range(0,len(list)):
        abc=abc+list[i]+"\n"

    return abc #해당 인덱스의 트랙 반환

#해당 id가 데이터에 있느냐 없느냐 검사 함수
def idCheck(usernumber):
    req = urllib.request.Request("http://ec2-18-216-35-115.us-east-2.compute.amazonaws.com:8000/student", headers={'User-Agent': 'Mozilla/5.0'})
    con = urllib.request.urlopen(req)
    text = con.read().decode("utf8")
    soup = BeautifulSoup(text, 'html.parser')

    sjnumber=soup.find_all("td",{'class',"number"})
    for n in sjnumber:
        i = sjnumber.index(n)
        sjnumber[i]= n.get_text().replace(" ","")
        sjnumber[i]=int(sjnumber[i])
    
    cnt=False
    for i in range(0,len(sjnumber)):
        if sjnumber[i]==usernumber:
            cnt=True
            break
    return cnt

#사용자 정보를 긁어와서 정보제공하는
def id(usernumber,num):
    global tuse
    global tbase
    global tname

    req = urllib.request.Request("http://ec2-18-216-35-115.us-east-2.compute.amazonaws.com:8000/student", headers={'User-Agent': 'Mozilla/5.0'})
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
        sjname[i]= n.get_text().replace(" ","")

    for n in sjnumber:
        i = sjnumber.index(n)
        sjnumber[i]= n.get_text().replace(" ","")
        sjnumber[i]=int(sjnumber[i])

    for n in sjtrack:
        i = sjtrack.index(n)
        sjtrack[i]= n.get_text().replace(" ","")

    for n in sjtrackbase:
        i = sjtrackbase.index(n)
        sjtrackbase[i]= n.get_text().replace(" ","")

    for n in sjtrackuse:
        i = sjtrackuse.index(n)
        sjtrackuse[i]= n.get_text().replace(" ","")

    trackread() #총 트랙 정리

    #입력한 학번에 대한 정보를 알기 위해 인덱스 추출
    for i in range(0,len(sjnumber)):
        if sjnumber[i]==usernumber:
            index1=i #index1=> 이름/학번/선택한 트랙
            break

    username=sjname[index1] #이름
    usertrack=[] #트랙이 2개 이상일수도 있으니 목록으로

    if sjtrack[index1].find(",")!=-1: #트랙이 2개 이상이면
        usertrack=sjtrack[index1].split(",")
        
    else: #트랙이 1개면
        usertrack.append(sjtrack[index1])

    #num1 => 트랙 과정
    if num==1:
        printstr=username+" 님은 "
        for i in range(0,len(usertrack)):
            printstr=printstr+","+usertrack[i]+' '
        printstr+="트랙 과정 중입니다.\n"
        return printstr

    #num2 => 기초 교과 수강한것과 수강하지않은 것 나눠서 
    elif num==2:
        printstr=""
        for j in range(0,len(usertrack)): #수강하고있는 트랙들
            printstr=printstr+username+" 님의 "+usertrack[j]+" 트랙 기초과정 현황입니다.\n\n"+"*수강한 교과목*\n"

            #해당 트랙 안에서 여태까지 수강한 기초교과목을 알려줌
            for i in range(0,len(tname)): #해당 트랙의 전체 교과과정을 알기 위한 전체 반복문
                if tname[i]==usertrack[j]: #해당 트랙의 인덱스를 찾음 => i
                    trackbase=tbase[i].split(",") #해당 트랙의 기초교과부분의 정보를 빼온 뒤 목록 생성
                    userbase=sjtrackbase[index1].split(",") #사용자가 현재 수강한 기초교과 목록 생성

                    for k in range(0,len(userbase)): #사용자가 수강한 기초교과가 해당 트랙의 기초교과 과목인지 확인하여
                        for l in range(0,len(trackbase)):
                            if userbase[k]==trackbase[l]: #맞다면
                                printstr=printstr+userbase[k]+"\n" #스트링에 추가함
                                
            printstr=printstr+"\n*수강해야하는 교과목*\n"

            #해당 트랙 안에서 여태까지 수강하지 않은 기초교과목을 알려줌
            for i in range(0,len(tname)):
                if tname[i]==usertrack[j]:
                    trackbase=tbase[i].split(",")
                    userbase=sjtrackbase[index1].split(",")

                    for k in range(0,len(trackbase)): #사용자가 수강한 기초교과를 뺀 나머지 교과목을 반환해주기위해
                        cnt=0
                        for l in range(0,len(userbase)): 
                            if userbase[l]==trackbase[k]: 
                                cnt+=1
                        if cnt==0:                  #만약 사용자가 수강하지않았다면 
                            printstr=printstr+trackbase[k]+"\n" #스트링에 추가함

            printstr+="\n===============\n"

        return printstr

    #num3=> 응용 교과 수강한 것과 수강하지 않은 것 나눠서
    elif num==3:
        printstr=""
        for j in range(0,len(usertrack)):
            printstr=printstr+username+" 님의 "+usertrack[j]+" 트랙 응용과정 현황입니다.\n\n"+"*수강한 교과목*\n"

            for i in range(0,len(tname)):
                if tname[i]==usertrack[j]:
                    trackuse=tuse[i].split(",")
                    useruse=sjtrackuse[index1].split(",")

                    for k in range(0,len(useruse)):
                        for l in range(0,len(trackuse)):
                            if useruse[k]==trackuse[l]:
                                printstr=printstr+useruse[k]+"\n"
                                
            printstr=printstr+"\n*수강해야하는 교과목*\n"

            for i in range(0,len(tname)):
                if tname[i]==usertrack[j]:
                    trackuse=tuse[i].split(",")
                    useruse=sjtrackuse[index1].split(",")

                    for k in range(0,len(trackuse)):
                        cnt=0
                        for l in range(0,len(useruse)):
                            if useruse[l]==trackuse[k]:
                                cnt+=1
                        if cnt==0:
                            printstr=printstr+trackuse[k]+"\n"

            printstr+="\n===============\n"

        return printstr


    elif num==4:
        for i in range(0,len(tname)):
            if tname[i]==usertrack[0]:
                trackbase=tbase[i].split(",")
                userbase=sjtrackbase[index1].split(",")
                cnt1=0
                for k in range(0,len(userbase)): 
                    for l in range(0,len(trackbase)):
                        if userbase[k]==trackbase[l]:
                            cnt1+=1

        score1 = cnt1/len(trackbase)*100

        for i in range(0,len(tname)):
            if tname[i]==usertrack[0]:
                trackuse=tuse[i].split(",")
                useruse=sjtrackuse[index1].split(",")
                cnt2=0
                for k in range(0,len(useruse)): 
                    for l in range(0,len(trackuse)):
                        if useruse[k]==trackuse[l]:
                            cnt2+=1
        score2 = cnt2/6.0*100

        uselist=[]
        for i in range(0,len(tname)):
                if tname[i]==usertrack[0]:
                    trackuse=tuse[i].split(",")
                    useruse=sjtrackuse[index1].split(",")

                    for k in range(0,len(trackuse)):
                        cnt=0
                        for l in range(0,len(useruse)):
                            if useruse[l]==trackuse[k]:
                                cnt+=1
                        if cnt==0:
                            uselist.append(trackuse[k])
        baselist=[]                    
        for i in range(0,len(tname)):
                if tname[i]==usertrack[0]:
                    trackbase=tbase[i].split(",")
                    userbase=sjtrackbase[index1].split(",")

                    for k in range(0,len(trackbase)):
                        cnt=0
                        for l in range(0,len(userbase)):
                            if userbase[l]==trackbase[k]:
                                cnt+=1
                        if cnt==0:
                            baselist.append(trackbase[k])
        

        printstr="http://interface518.dothome.co.kr/test.php?data1=%.2f&data2=%.2f&name=%s&track=%s&use1=%s&use2=%s&base1=%s&base2=%s"%(score1,score2,username,usertrack[0],useruse,uselist,userbase,baselist)
        
        return printstr