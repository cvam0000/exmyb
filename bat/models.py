
from django.conf import settings
from django.db import models
from django.utils import timezone


class Bat_textquestions(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    s_no = models.CharField(max_length=10,null=True)
    title = models.CharField(max_length=200)
    question = models.TextField()
    enable_when_question_no = models.CharField(max_length=10,null=True)
    is_dependent_question_no= models.CharField(max_length=10,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



    def __str__(self):
        return str(self.user)


class Mcq(models.Model):
    author = models.ForeignKey(Bat_textquestions, on_delete=models.CASCADE)
    questions = models.TextField()
    question_no = models.CharField(max_length=10, unique=True,null=True)
    enable_when_question_no = models.CharField(max_length=10,null=True)
    choice1 = models.CharField(max_length=200, unique=True,null=True)
    choice2 = models.CharField(max_length=200, unique=True,null=True)
    choice3 = models.CharField(max_length=200, unique=True,null=True)
    choice4 = models.CharField(max_length=200, unique=True,null=True)
    choice5 = models.CharField(max_length=200, unique=True,null=True)
    choice6 = models.CharField(max_length=200, unique=True,null=True)
    choice7 = models.CharField(max_length=200, unique=True,null=True)
    choice8 = models.CharField(max_length=200, unique=True,null=True)
    choice9 = models.CharField(max_length=200, unique=True,null=True)
    choice10 = models.CharField(max_length=200, unique=True,null=True)
    choice11 = models.CharField(max_length=200, unique=True,null=True)
    choice12 = models.CharField(max_length=200, unique=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()
   

   

