from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from dataviewer.models import Data


'''
데이터베이스에 있는 내용을, 웹브라우저에 어떻게 보여줄지 정의

함수형태로 정의


Request에 대응하는 Response주는 파일
'''

def helloworld(request):
    data = Data.objects.all()
    return render(request, 'dataviewer/helloworld.html', {
        'data': data
    })

def helloworld_json(request):
    # django orm => queryset
    data = Data.objects.all().values('key', 'value')
    print(type(list(data)))
    return JsonResponse({'data': list(data)})