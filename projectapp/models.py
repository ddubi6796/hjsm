from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now=True)

    #프로젝트를 '프로젝트순번:프로젝트명' 형태로 나타내어 주기 위함
    def __str__(self):
        return f'{self.pk} : {self.title}'