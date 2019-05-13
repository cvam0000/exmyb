
from django.conf import settings
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    profile_tag = models.CharField(max_length=200)
    Type_of_funding = models.CharField(max_length=200)
    Reason = models.CharField(max_length=500)
    Industries= models.TextField()
    Location= models.CharField(max_length=200)
    Business_overview= models.TextField()
    Total_investment=models.CharField(max_length=500)
    capital_assesst_investment=model.Charfield(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title