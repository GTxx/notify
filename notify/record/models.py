from django.db import models

# Create your models here.

class PickUp(models.Model):
    center = models.IntegerField()
    klass = models.IntegerField()
    student = models.IntegerField()
    student_name = models.CharField(max_length=32)
    pickup = models.CharField(max_length=32, blank=True, null=True)
    time = models.CharField(max_length=16)
    date = models.DateField()

