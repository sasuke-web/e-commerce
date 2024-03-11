from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
