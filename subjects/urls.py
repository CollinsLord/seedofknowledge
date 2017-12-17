from django.urls import path
from . import views

app_name = 'subjects'
urlpatterns = [
    path('list', views.SubjectList.as_view(), name='subject-list'),
    path('<int:pk>', views.SubjectDetail.as_view(), name='subject-detail'),
]
