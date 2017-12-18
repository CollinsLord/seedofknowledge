from django.db import models
from django.urls import reverse 
from subjects.models import Subject

class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
