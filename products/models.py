from projects.models import Donor
from django.db import models
from accounts.models import Hub
from phonenumber_field.modelfields import PhoneNumberField
from products.constants import (
    BRAND_CHOICES,
    COMPUTER_STATUS_CHOICES,
    MONITOR_STATUS_CHOICES,
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
    DRAM,
    LINUX,
    HDD,
    PROCESSED,
    REFURBISHED,
    SCREEN_SIZE_CHOICES,
    PAYMENT_METHOD,
    SUPPLIER_CATEGORY,
    )

class Operating_System(models.Model):
    os_name = models.CharField(max_length=100)

    def __str__(self):
        return self.os_name

class Operating_system_Version(models.Model):
    os_name = models.ForeignKey(Operating_System, on_delete=models.CASCADE)
    os_version = models.CharField(max_length=100)

    def __str__(self):
        return self.os_version

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255,default=None, blank=True, null=True)
    address = models.CharField(max_length=100)
    contact = PhoneNumberField(blank=True)
    contact_2 = PhoneNumberField(default=None, blank=True, null=True)
    contact_person = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_METHOD, default=None, blank=True)
    supplier_email = models.EmailField(blank=True, default=None, null=True)
    supplier_email_2 = models.EmailField(blank=True, default=None, null=True)
    supplier_website = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    supplier_category = models.CharField(max_length=20, choices=SUPPLIER_CATEGORY, default=None, blank=True)
    supplier_items = models.CharField(max_length=255,default=None, blank=True, null=True, help_text='ie. Laptops, Printers, Desktops, Networking Materials, Accessories, Tablets, Electric Supplies. Please use comma(,) to separate the items.')
    supplier_items_status = models.CharField(max_length=255, blank=True, null=True, help_text='ie. Brand New, Used, Refurb, Both. Please use comma(,) to separate the items.')

    def __str__(self):
        return self.name

class Computer(models.Model):
    hub = models.ForeignKey(Hub,on_delete=models.CASCADE, default=None, null=True)
    c_affritrack_number = models.CharField(max_length=50, null=True, default=None, blank=True)
    serial_number = models.CharField(max_length=50, null=True, default=None, blank=True,)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    model = models.CharField(max_length=30)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, null=True, default=REFURBISHED)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    processor_type = models.CharField(max_length=20, choices=PROCESSOR_TYPE_CHOICES)
    processor_speed = models.CharField(max_length=10)
    memory_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES, default=DRAM)
    memory_size = models.CharField(max_length=10, choices=RAM_SIZE_CHOICES)
    storage_type = models.CharField(max_length=10, choices=STORAGE_TYPE_CHOICES, default=HDD)
    storage_size = models.CharField(max_length=10, choices=STORAGE_SIZE_CHOICES)
    os_type = models.ForeignKey(Operating_System, on_delete=models.CASCADE, null=True, default=None, blank=True)
    os_version = models.ForeignKey(Operating_system_Version, on_delete=models.CASCADE, null=True, default=None, blank=True)
    working_status = models.CharField(max_length=30, choices=COMPUTER_STATUS_CHOICES, default=WORKING)
    date_received = models.DateField()
    comment = models.CharField(null=True, default=None, blank=True, max_length=240)
    screen_size = models.CharField(max_length=20, choices=SCREEN_SIZE_CHOICES, default=INCH17)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES, default=SYSTEM_UNIT)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.c_affritrack_number


class Monitor(models.Model):
    hub = models.ForeignKey(Hub,on_delete=models.CASCADE, default=1, null=True)
    m_affritrack_number = models.CharField(max_length=50, null=True, default=None, blank=True)
    serial_number = models.CharField(max_length=50, null=True, default=None, blank=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    container_number = models.CharField(max_length=20)
    device_status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, null=True, default=REFURBISHED)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    date_received = models.DateField()
    screen_size = models.CharField(max_length=20, choices=SCREEN_SIZE_CHOICES, default=INCH17)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, default=None, blank=True,)
    comment = models.CharField(null=True, default=None, blank=True, max_length=240)
    working_status = models.CharField(max_length=30, choices=MONITOR_STATUS_CHOICES, default=PROCESSED)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.m_affritrack_number

