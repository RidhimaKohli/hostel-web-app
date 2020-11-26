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
    HOSTEL_CHOICES=(
        ('B1','B1'),
        ('B2','B2'),
        ('B3','B3'),
        ('B4','B5'),
        ('G1','G1'),
        ('G2','G2'),
        ('G3','G3'),
        ('G4','G4'),
        ('G5','G5'),
        ('G6','G6'),
        ('I2','I2')
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    complaint_pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    hostel=models.CharField(max_length=2, choices=HOSTEL_CHOICES, default='B1')

