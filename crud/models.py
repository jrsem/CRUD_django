import email
from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.email} {self.address} {self.phone}"
