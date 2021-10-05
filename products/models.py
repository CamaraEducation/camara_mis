from django.db.models.enums import Choices
from projects.models import Donor
from products.constants import (
    BRAND_CHOICES,
    COMPUTER_STATUS_CHOICES,
    DEVICE_STATUS_CHOICES,
    OS_TYPE_CHOICES,
    PROCESSOR_TYPE_CHOICES,
    RAM_SIZE_CHOICES,
    RAM_TYPE_CHOICES,
    STORAGE_SIZE_CHOICES,
    STORAGE_TYPE_CHOICES,
    DEVICE_TYPE_CHOICES,
    SYSTEM_UNIT,)
    
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
    c_affritrack_number = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    model = models.CharField(max_length=30)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    processor_type = models.CharField(max_length=20, choices=PROCESSOR_TYPE_CHOICES)
    processor_speed = models.CharField(max_length=10)
    memory_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES)
    memory_size = models.CharField(max_length=10, choices=RAM_SIZE_CHOICES)
    storage_type = models.CharField(max_length=10, choices=STORAGE_TYPE_CHOICES)
    storage_size = models.CharField(max_length=10, choices=STORAGE_SIZE_CHOICES)
    os_type = models.CharField(max_length=10, choices=OS_TYPE_CHOICES)
    os_version = models.CharField(max_length=30)
    working_status = models.CharField(max_length=30, choices=COMPUTER_STATUS_CHOICES)
    date_received = models.DateField()
    # price
    # cost
    screen_size = models.CharField(max_length=20, default='21')
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES, default=SYSTEM_UNIT)
    def __str__(self):
        return self.c_affritrack_number


class Monitor(models.Model):
    m_affritrack_number = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_received = models.DateField()
    screen_size = models.CharField(max_length=20, default='21')
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    working_status = models.CharField(max_length=30, choices=COMPUTER_STATUS_CHOICES)
    # price
    # cost

    def __str__(self):
        return self.m_affritrack_number