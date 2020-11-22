from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    teacher = models.ManyToManyField('Teacher')



class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    subject = models.ManyToManyField('Subject')


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
