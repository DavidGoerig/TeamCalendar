from django.db import models

# Create your models here.

class DevicesTypes(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Devices(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=80, default="0")
    sap_equipment_nbr = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    reservation_status = models.BooleanField(default=False)
    start_date = models.DateField(default=None,blank=True, null=True)
    end_date = models.DateField(default=None,blank=True, null=True)
    def __str__(self):
        return self.name + " SN: " + self.serial_number

class Area(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name