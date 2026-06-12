from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  

class Profile(models.Model):
  bio = models.TextField(max_length=500)
  location = models.CharField(max_length=100)
  birt_date = models.DateField(null=True,blank=True)

  def __str__(self):
    return str(self.location)