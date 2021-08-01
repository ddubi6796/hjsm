from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld    # Alt+Ent: auto import


has_ownership = [account_ownership_required, login_required]

@login_required
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

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User  # 장고가 제공하는 기본 유저 클래스
    context_object_name = 'target_user'
    form_class = AccountUpdateForm  # 커스터마이징한 form
    success_url = reverse_lazy('accountapp:hello_world')  # 함수와 클래스간의 import 방식의 차이로 인해 reverse 함수 사용 불가
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User  # 장고가 제공하는 기본 유저 클래스
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
