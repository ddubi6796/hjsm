from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView
from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name="subscribe"),
]