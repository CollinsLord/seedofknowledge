from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('list/', views.CourseList.as_view(), name='course-list'),
]
