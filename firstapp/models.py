from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.IntegerField()


def __str__(self):
    return self.name
