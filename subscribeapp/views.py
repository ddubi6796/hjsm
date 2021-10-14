from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # 해당 project_pk를 가진 프로젝트가 없을 경우 404에러 발생
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # 구독 정보가 있을 경우 delete, 없을 경우 생성
        subscription = Subscription.objects.filter(user=user, project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') #user가 구독한 프로젝트 리스트
        article_list = Article.objects.filter(project__in=projects) #user가 구독한 project 리스트에 해당하는 article
        return article_list