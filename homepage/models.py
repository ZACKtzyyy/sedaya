from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    role = (
        ("regular","Regular"),
        ("member","Member")
    )


    student_id = models.CharField(max_length=20)
    agreed_to_terms = models.BooleanField(default=False)
    role = models.CharField(max_length=10,choices=role,default="regular")

class Events(models.Model):
    eventsID = models.CharField(max_length=100 , primary_key=True)
    eventsName = models.TextField(max_length=100)
    eventsDesc = models.CharField(max_length=100)
    eventsDate = models.DateField()

class Membership(models.Model):
    memberid = models.CharField(max_length=20)
    student_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    membernohp = models.CharField(max_length=15)
    memberdate = models.DateField(auto_now=True)
    musicinstrument = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("membership")

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

class Achievement(models.Model):
    achname = models.CharField(max_length=100)
    achdesc = models.TextField()
    achvenue = models.CharField(max_length=100)
    achdate = models.DateField()
    achstanding = models.IntegerField()
    achcategory = models.CharField(max_length=50)

    def __str__(self):
        return self.achname






