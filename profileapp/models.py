from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # profile과 user객체를 연결해주는 내장 함수
    # CASCADE user 객체 delete 시 profile도 삭제되도록
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # settings.py 내 MEDIA_ROOT에서 정의한 디렉터리 하위에 해당 경로 생성 후 업로드
    image = models.ImageField(upload_to='profile/', null=True) #nullable

    nickname = models.CharField(max_length=20, unique=True, null=True) #중복방지
    message = models.CharField(max_length=100, null=True)
