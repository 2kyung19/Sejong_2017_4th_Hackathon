from django.shortcuts import render
from django.http import JsonResponse

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['상록원', '그루터기', '아리수', '기숙사식당', '교직원식당']
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가

    return return_str