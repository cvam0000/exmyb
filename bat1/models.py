from django.conf import settings
from django.db import models
from django.utils import timezone


class Bat1_ques(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Answers_Bat1(models.Model):
    answers1 = models.CharField(max_length=200)
    answers2 = models.CharField(max_length=200)
    answers3 = models.CharField(max_length=200)
    answers4 = models.CharField(max_length=200)
    answers5 = models.CharField(max_length=200)
    answers6 = models.CharField(max_length=200)
    answers7 =models.CharField(max_length=200)
    answers8 = models.CharField(max_length=200)
    answers9 = models.CharField(max_length=200)
    answers10 = models.CharField(max_length=200)
    answers11 = models.CharField(max_length=200)
    answers12 = models.CharField(max_length=200)

