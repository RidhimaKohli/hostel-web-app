from django.db import models

# Create your models her
class complain(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=12)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    date = models.DateField()

