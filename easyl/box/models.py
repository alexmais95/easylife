from django.db import models
from phone_field import PhoneField
from languages.fields import LanguageField
from django_countries.fields import CountryField



class Client(models.Model):
    id_by_tg = models.IntegerField(primary_key=True)
    name_tg = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    language = models.CharField()
    country = models.CharField()
    code_warification = models.IntegerField()

    def __str__(self) -> str:
        return self.name_tg

class Box(models.Model):
    id_box = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    summ = models.DecimalField(max_digits=6, decimal_places=2)
    choice = models.IntegerField()
    type_distrybushin = models.CharField()
    summ_now = models.CharField()
    distrybushim_now = models.CharField()
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.name


class UserBox(models.Model):
    id_by_tg = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_box = models.ForeignKey('Box', on_delete=models.CASCADE)
    

class Operation(models.Model):
    id_by_tg = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_box = models.ForeignKey('Box', on_delete=models.CASCADE)
    summ = models.DecimalField(max_digits=6, decimal_places=2)
    nom_operation = models.IntegerField()
    time = models.TimeField(auto_now=True)
    status =  models.CharField()

class Balance(models.Model):
    id_user = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_coin = models.ForeignKey('Coin', on_delete=models.CASCADE)

class Coin(models.Model):
    id_coin = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    numb_coin = models.IntegerField()
    status =  models.CharField()

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    id_news = models.BigAutoField(primary_key=True)
    text = models.TextField()

class MassageUser(models.Model):
    id_user = models.ForeignKey('Client', on_delete=models.CASCADE)
    id_news = models.ForeignKey('News', on_delete=models.CASCADE)
    date = models.DateField()




