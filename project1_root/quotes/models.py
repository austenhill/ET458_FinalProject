import email
from operator import mod
from tkinter.tix import Tree
from turtle import position
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('FR', 'Freshman'),
    ('SP', 'Sophmore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
)

PRIORITY_CHOICES = (
    ('1', '2015'),
    ('2', '2016'),
    ('3', '2017'),
    ('4', '2018'),
    ('5', '2019'),
    ('6', '2020'),
    ('7', '2021'),
    ('8', '2022')
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    bio = models.TextField()
    major = models.CharField(max_length=60, blank=True)
    classification = models.CharField(max_length=20, choices=STATUS_CHOICES)
    graduation = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    skills = models.TextField()
    languages = models.CharField(max_length=100)
    experience = models.TextField()
    picture = models.FileField(upload_to='uploads/', blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
