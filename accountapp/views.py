from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld    # Alt+Ent: auto import


def hello_world(request):
    # return HttpResponse('안녕하세요 HJSM의 첫번째 View입니다!!')

    # OST와 GET방식 분기
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User  # 장고가 제공하는 기본 유저 클래스
    form_class = UserCreationForm   # model을 사용하기 위하여 장고가 기본 제공하는 form
    success_url = reverse_lazy('accountapp:hello_world')  # 함수와 클래스간의 import 방식의 차이로 인해 reverse 함수 사용 불가
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'