from django.db.models.enums import Choices
from django.forms import widgets
from projects.models import Donor
from accounts.models import Hub
from products.constants import (
    BRAND_CHOICES,
    COMPUTER_STATUS_CHOICES,
    DEVICE_STATUS_CHOICES,
    INCH17,
    OS_TYPE_CHOICES,
    PROCESSOR_TYPE_CHOICES,
    RAM_SIZE_CHOICES,
    RAM_TYPE_CHOICES,
    STORAGE_SIZE_CHOICES,
    STORAGE_TYPE_CHOICES,
    DEVICE_TYPE_CHOICES,
    SYSTEM_UNIT,
    WORKING,
    PROCESSED,
    REFURBISHED,
    SCREEN_SIZE_CHOICES,)
    
from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Computer(models.Model):
    hub = models.ForeignKey(Hub,on_delete=models.CASCADE, default=1, null=True)
    c_affritrack_number = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    model = models.CharField(max_length=30)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, null=True, default=REFURBISHED)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    processor_type = models.CharField(max_length=20, choices=PROCESSOR_TYPE_CHOICES)
    processor_speed = models.CharField(max_length=10)
    memory_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES)
    memory_size = models.CharField(max_length=10, choices=RAM_SIZE_CHOICES)
    storage_type = models.CharField(max_length=10, choices=STORAGE_TYPE_CHOICES)
    storage_size = models.CharField(max_length=10, choices=STORAGE_SIZE_CHOICES)
    os_type = models.CharField(max_length=10, choices=OS_TYPE_CHOICES, null=True)
    os_version = models.CharField(max_length=30, null=True)
    working_status = models.CharField(max_length=30, choices=COMPUTER_STATUS_CHOICES, default=WORKING)
    date_received = models.DateField()
    # price
    # cost
    screen_size = models.CharField(max_length=20, choices=SCREEN_SIZE_CHOICES, default=INCH17)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES, default=SYSTEM_UNIT)
    def __str__(self):
        return self.c_affritrack_number


class Monitor(models.Model):
    hub = models.ForeignKey(Hub,on_delete=models.CASCADE, default=1, null=True)
    m_affritrack_number = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, null=True, default=REFURBISHED)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    date_received = models.DateField()
    screen_size = models.CharField(max_length=20, choices=SCREEN_SIZE_CHOICES, default=INCH17)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    working_status = models.CharField(max_length=30, choices=COMPUTER_STATUS_CHOICES, default=PROCESSED)
    # price
    # cost

    def __str__(self):
        return self.m_affritrack_number