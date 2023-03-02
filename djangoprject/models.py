from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=True, null=False)
    phone_num = models.IntegerField(max_length=50, blank=True, null=False)

def __str__(self):
    return self.name