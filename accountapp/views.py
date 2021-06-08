from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    #return HttpResponse('안녕하세요 HJSM의 첫번째 View입니다!!')

    #POST와 GET방식 분기
    if request.method == "POST":
        return render(request, 'accountapp/helloworld.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET METHOD!!!'})
