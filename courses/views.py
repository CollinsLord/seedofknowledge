from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

class CourseList(ListView):
    model = Course

class CourseDetails(DetailView):
    model = Course
