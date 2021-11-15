from django.db import models
from django.utils import tree
from accounts.models import Hub, UserProfile

from products.constants import (
    DEVICE_TYPE_CHOICES,
    DEVICE_STATUS_CHOICES,
    PROCESSOR_TYPE_CHOICES,
    RAM_TYPE_CHOICES,
    RAM_SIZE_CHOICES,
    STORAGE_TYPE_CHOICES,
    STORAGE_SIZE_CHOICES,
    OS_TYPE_CHOICES
)
from school.models import School
from projects.models import Project
# Create your models here.

class Computer_Applicant(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, default=None)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.full_name

class Computer_Request(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    number_of_computers = models.IntegerField(help_text="Number of computers requesting")
    applicant_id = models.ForeignKey(Computer_Applicant, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True, null=True)
    invoice_number = models.CharField(max_length=100, help_text="Invoice Number",blank=True, default=None, null=True)
    computer_type = models.CharField(max_length=30, choices=DEVICE_TYPE_CHOICES,blank=True, default=None, help_text="If its laptop, CPU, tablet etc", null=True)
    computer_status = models.CharField(max_length=30, choices=DEVICE_STATUS_CHOICES,blank=True, default=None, null=True)
    processor_type = models.CharField(max_length=30, choices=PROCESSOR_TYPE_CHOICES,blank=True, default=None, null=True)
    processor_speed = models.CharField(max_length=30,blank=True, default=None, null=True)
    memory_type = models.CharField(max_length=30, choices=RAM_TYPE_CHOICES,blank=True, default=None, null=True)
    memory_size = models.CharField(max_length=30, choices=RAM_SIZE_CHOICES,blank=True, default=None, null=True)
    storage_type = models.CharField(max_length=30, choices=STORAGE_TYPE_CHOICES,blank=True, default=None, null=True)
    storage_size = models.CharField(max_length=30, choices=STORAGE_SIZE_CHOICES,blank=True, default=None, null=True)
    os_type = models.CharField(max_length=30, choices=OS_TYPE_CHOICES,blank=True, default=None, null=True)
    os_version = models.CharField(max_length=30,blank=True, default=None, null=True)
    request_notes = models.CharField(max_length=250,blank=True, default=None, null=True)
    request_status = models.IntegerField(default=0, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name

class Dispatch(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    computer_request_id = models.ForeignKey(Computer_Request, on_delete=models.CASCADE)
    applicant_name = models.ForeignKey(Computer_Applicant, on_delete=models.CASCADE)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    c_affritrack_number = models.CharField(max_length=50)
    m_affritrack_number = models.CharField(max_length=50)
    date_dispatched = models.DateField()
    dispatched_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    warranty_end = models.DateField()