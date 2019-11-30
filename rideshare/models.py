from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254)
    driving_license = models.CharField(max_length=15, blank=True, default='')
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.first_name + self.last_name

class Kid(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254, blank=True, default='')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name
