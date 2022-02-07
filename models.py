from django.db import models

class Package(models.Model):
    packagename = models.CharField(max_length=20, default=None)
    price = models.CharField(max_length=10, default=None)
    image = models.ImageField(upload_to="images", default='')
    about = models.TextField(max_length=50, default=None)
class Login(models.Model):

    name = models.CharField(max_length=25, default=None)
    password = models.CharField(max_length=25, default=None)
    email = models.CharField(max_length=10, default=None)

class Admin(models.Model):
    name = models.CharField(max_length=25, default=None)
    password = models.CharField(max_length=25, default=None)

































