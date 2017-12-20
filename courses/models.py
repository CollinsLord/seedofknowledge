from django.db import models
from django.urls import reverse 
from subjects.models import Subject, Unit
from datetime import datetime

class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.name

    def save(self, *args, **kwargs):
        new = self.pk is None
        super().save(*args, **kwargs)
        if new:
            subject = self.subject
            units = Unit.objects.filter(subject=subject)
            for unit in units:
                lecture = Lecture(course=self, unit=unit.name, 
                        date=datetime.today(), start_time=datetime.now(), 
                        end_time=datetime.now())
                lecture.save()

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return "{} on {} ({} - {})".format(self.course, self.date, 
                self.start_time, self.end_time)


