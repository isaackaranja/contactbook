from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'contact name is {self.name}'
