from django.db import models
from django.utils import timezone


class Loginfo(models.Model):
    name = models.CharField(max_length=283)
    department = models.CharField(choices =[
        ('SD','Software Development'),('STV','Software Testing'),('HR','Human Resources'),
        ('DS','Data Science')
    ],default = 'SD', max_length = 4)
    staff_id = models.IntegerField()
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
# Create your models here.


class VisitorInfo(models.Model):
    name = models.CharField(max_length=283)
    visitor_name = models.CharField(max_length=283)
    visitor_department = models.CharField(choices =[
        ('SD','Software Development'),('STV','Software Testing'),('HR','Human Resources'),
        ('DS','Data Science')
    ],default = 'SD', max_length = 4)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


