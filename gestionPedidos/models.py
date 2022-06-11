from django.db import models

# Create your models here.
from unicodedata import name


class Client(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, verbose_name='La direccion')
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return 'Nombre: %s' % ( self.name )


class Article(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return 'Name %s, section %s, price %s' % (self.name, self.section, self.amount)


class Order(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
