from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=15)
    room_number = models.IntegerField()
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None)
    is_secretary = models.BooleanField(default=False)
    

class Complaint(models.Model):
    content = models.TextField(max_length=500)
    title = models.CharField(max_length=100)
    complaint_pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


