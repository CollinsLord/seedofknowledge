from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Subject

class SubjectList(ListView):
    model = Subject

class SubjectDetail(DetailView):
    model = Subject
