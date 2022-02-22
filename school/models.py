import re
from statistics import mode
from django.db import models
from projects.models import Project
from accounts.models import Hub
from phonenumber_field.modelfields import PhoneNumberField
from school.constants import SCHOOL_AREA_CHOICES, SCHOOL_LEVEL_CHOICES, SCHOOL_OWNERSHIP_CHOICES
# Create your models here.

class County_Region(models.Model):
    hub_name = models.ForeignKey(Hub, on_delete=models.CASCADE, null=True, default=None, blank=True)
    county_or_region_name = models.CharField(max_length=30)

    def __str__(self):
        return self.county_or_region_name

class Sub_County_Zone (models.Model):
    county_or_region_name = models.ForeignKey(County_Region, on_delete=models.CASCADE)
    sub_county_or_Zone_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_county_or_Zone_name

class District_Woreda(models.Model):
    county_or_region_name = models.ForeignKey(County_Region, on_delete=models.CASCADE)
    sub_county_or_Zone_name = models.ForeignKey(Sub_County_Zone, on_delete=models.CASCADE)
    district_or_woreda_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_or_woreda_name

class School(models.Model):
    school_code = models.CharField(max_length=20, unique=True, blank=True, default=None, null=True)
    country = models.ForeignKey(Hub, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    school_level = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES, blank=True, default=None, null=True)
    school_ownership = models.CharField(max_length=20, choices=SCHOOL_OWNERSHIP_CHOICES, blank=True, default=None, null=True)
    school_area = models.CharField(max_length=20, choices=SCHOOL_AREA_CHOICES, blank=True, default=None, null=True)
    po_box = models.CharField(max_length=20, default=None, blank=True, null=True)
    phone_number_1= PhoneNumberField(default=None, blank=True, null=True)
    phone_number_2 = PhoneNumberField(default=None, blank=True, null=True)
    email = models.EmailField(max_length=20, default=None, blank=True, null=True)
    website = models.CharField(max_length=20, default=None, blank=True, null=True)
    female_teachers = models.IntegerField(default=0)
    male_teachers = models.IntegerField(default=0)
    female_students = models.IntegerField(default=0)
    male_students = models.IntegerField(default=0)
    female_sn_students = models.IntegerField(default=0)
    male_sn_students = models.IntegerField(default=0)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, default=None, blank=True)
    county_or_region_name = models.ForeignKey(County_Region, on_delete=models.CASCADE, null=True, default=None, blank=True)
    sub_county_or_Zone_name = models.ForeignKey(Sub_County_Zone, on_delete=models.CASCADE, null=True, default=None, blank=True)
    district_or_woreda_name = models.CharField(max_length=30, default=None, blank=True, null=True)

    def __str__(self):
        return self.school_name

