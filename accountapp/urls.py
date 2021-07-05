from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"  ##브라우저에서 hello_world에 접근할때 aacountapp:hello_word만으로 접근할 수 잇도록 해줌.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 함수형 View

    path('create/', AccountCreateView.as_view(), name='create') # 클래스형 View
]