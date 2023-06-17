from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=50)
    houseloc=models.CharField(max_length=50)
    email=models.CharField( max_length=70)
    phone=models.CharField( max_length=12)
    #location=models.JSONField(_(""), encoder=, decoder=)
    desc=models.CharField(max_length=500)
    rentprice=models.IntegerField()
    noroom=models.IntegerField()

class Owner(models.Model):
    name=models.CharField( max_length=50)
    houseloc=models.CharField(max_length=50)
    email=models.CharField( max_length=70)
    phone=models.CharField( max_length=12)
    #location=models.JSONField(_(""), encoder=, decoder=)
    desc=models.CharField(max_length=500)
    rentprice=models.IntegerField()
    noroom=models.IntegerField()