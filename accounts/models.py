from django.db import models
# from django.db.models.base import Model
from .constants import (COUNTRY_CHOICES, REGISTRATION_STATUS_CHOICES,
                        EMPLOYEMENT_TYPE_CHOICES, EDUCATION_LEVEL_CHOICES,
                        USER_CONTACT_RELATIONSHIP_CHOICES, GENDER_CHOICES)
from django.contrib.auth.models import User


from phonenumber_field.modelfields import PhoneNumberField

class Hub(models.Model):
    hub_code = models.CharField(max_length=20,unique=True)
    hub_name = models.CharField(max_length=100)
    hub_located_country = models.CharField(max_length=30, choices=COUNTRY_CHOICES)
    hub_address = models.CharField(max_length=100,blank=True, default=None, null=True)
    hub_email = models.EmailField()
    hub_phone = PhoneNumberField(blank=True)
    hub_registration_year = models.DateField()
    hub_registration_number = models.CharField(max_length=100)
    hub_registration_status = models.CharField(max_length=30, choices=REGISTRATION_STATUS_CHOICES)
    hub_tin_number = models.CharField(max_length=100)
    hub_country_director = models.ForeignKey(User, on_delete=models.CASCADE)
    hub_website = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_facebook = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_instagram = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_twitter = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_linkedin = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_youtube = models.CharField(max_length=100, default=None, blank=True, help_text='Optional')
    hub_status = models.IntegerField(default=1)

    def __str__(self):
        return self.hub_name

class Department(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    department_code = models.CharField(max_length=50, unique=True)
    department_name = models.CharField(max_length=100)
    department_email = models.EmailField(default=None, blank=True)
    department_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    department_phone_number = PhoneNumberField(blank=True)
    department_role = models.CharField(max_length=100,blank=True, default=None, null=True)

    def __str__(self):
        return self.department_name

class Position(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position_name = models.CharField(max_length=100)
    position_description = models.CharField(max_length=100,blank=True, default=None, null=True)

    def __str__(self):
        return self.position_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    user_code = models.CharField(max_length=100, unique=True)
    user_personal_email = models.EmailField(blank=True, default=None, null=True)
    user_hired_date = models.DateField()
    user_employement_type = models.CharField(max_length=20, choices=EMPLOYEMENT_TYPE_CHOICES)
    user_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    user_phone_number = PhoneNumberField(blank=True)
    user_education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    user_birth_date = models.DateField()
    user_contact_name = models.CharField(max_length=100, blank=True, default=None, null=True)
    user_contact_phone_number = PhoneNumberField(blank=True, default='+251935629442')
    user_contact_email = models.EmailField(blank=True, default=None, null=True)
    user_contact_address = models.CharField(max_length=100,blank=True, default=None, null=True)
    user_contact_relationship = models.CharField(max_length=30, choices=USER_CONTACT_RELATIONSHIP_CHOICES)

    def __str__(self):
        return self.user.username