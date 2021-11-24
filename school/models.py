from django.db import models

from accounts.models import Hub
from school.constants import SCHOOL_AREA_CHOICES, SCHOOL_LEVEL_CHOICES, SCHOOL_OWNERSHIP_CHOICES
# Create your models here.

class School(models.Model):
    school_code = models.CharField(max_length=20, unique=True, blank=True, default=None)
    country = models.ForeignKey(Hub, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    school_level = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)
    school_ownership = models.CharField(max_length=20, choices=SCHOOL_OWNERSHIP_CHOICES)
    school_area = models.CharField(max_length=20, choices=SCHOOL_AREA_CHOICES)
    po_box = models.CharField(max_length=20, default=None, blank=True)
    phone_number_1= models.CharField(max_length=20, default=None, blank=True)
    phone_number_2 = models.CharField(max_length=20, default=None, blank=True)
    email = models.EmailField(max_length=20, default=None, blank=True, null=True)
    website = models.CharField(max_length=20, default=None, blank=True)
    female_teachers = models.IntegerField(default=0)
    male_teachers = models.IntegerField(default=0)
    female_students = models.IntegerField(default=0)
    male_students = models.IntegerField(default=0)
    female_sn_students = models.IntegerField(default=0)
    male_sn_students = models.IntegerField(default=0)

    def __str__(self):
        return self.school_name