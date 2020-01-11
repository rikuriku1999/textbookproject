from django.db import models

# Create your models here.

class Textbookmodel(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='', null=True ,blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    goodtext = models.CharField(max_length=200, null=True, blank=True, default='a')
    

class Commentmodel(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

class Usermodel(models.Model):
    nickname = models.CharField(max_length=50)
    intro = models.TextField(blank=True,default='')
