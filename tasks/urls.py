from django.urls import path
from .views import TaskCreateView, TaskViewGet, IDTaskAPIView

urlpatterns = [
    path('list', TaskViewGet.as_view(),),
    path('add', TaskCreateView.as_view(),),
    path('up', IDTaskAPIView.as_view()),
]