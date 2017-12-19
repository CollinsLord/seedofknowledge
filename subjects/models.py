from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("number", "subject")
        ordering = ["subject", "number"]

