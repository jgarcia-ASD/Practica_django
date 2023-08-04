from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class Author(models.Model):
    documento = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank = False)

    def __str__(self):
        return self.nickname


