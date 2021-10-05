from django.db import models
from django.db.models import manager
from django_countries.fields import CountryField
from .constants import DONATION_CATEGORY_CHOICES, DONOR_TYPE_CHOICES
from django.contrib.auth.models import User
from accounts.models import Hub

# Create your models here.
class Project(models.Model):
	project_code = models.CharField(max_length=100, unique=True)
	project_name = models.CharField(max_length=100)
	hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
	project_manager = models.ForeignKey(User, on_delete=models.CASCADE)
	project_description = models.TextField()
	project_start_date = models.DateField()
	project_end_date = models.DateField()
	project_budget = models.CharField(max_length=100)

	def __str__(self):
		return self.project_name

class Donor(models.Model):
	donor_name = models.CharField(max_length=100)
	donor_description = models.TextField(default=None, blank=True, help_text="Short Description of the Donor and what the donor normally funds")
	donor_website = models.CharField(max_length=100, default=None, blank=True)
	donor_dates = models.DateField(default=None, blank=True, help_text = "Key Dates for donation or funding application submission")
	donor_email = models.EmailField()
	country = CountryField()
	donor_contact = models.CharField(max_length=100, default=None, blank=True)
	donation_range = models.IntegerField(help_text="Range of How much Funds the Donor Normally Provide")
	donation_category = models.CharField(max_length=30, choices=DONATION_CATEGORY_CHOICES)
	donor_type = models.CharField(max_length=30, choices=DONOR_TYPE_CHOICES)
	key_contact_name = models.CharField(max_length=100,default=None, blank=True)
	key_contact_email = models.EmailField(default=None, blank=True)

	def __str__(self):
		return self.donor_name

class Partner(models.Model):
	partner_name = models.CharField(max_length=100)
	partner_adress = models.CharField(max_length=250)
	partner_country = CountryField()
	key_contact_name = models.CharField(max_length=100)
	key_contact_email = models.EmailField()
	partner_website = models.CharField(max_length=200, blank=True, default=None)
	partner_description = models.TextField(blank=True, default=None, help_text="Short description of the partners expertise and how it fits with Camara")
	partnership_start = models.DateField()
	areas_of_patnership = models.TextField(help_text="Agreed areas of partnership")
	# partner_mou = models.FileField(help_text="Copy of the MOU with the partner (if any)")

	def __str__(self):
		return self.partner_name

class Project_Partner(models.Model):
	project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
	partner_name = models.ForeignKey(Partner, on_delete=models.CASCADE)
	partner_role = models.CharField(max_length=200, default=None, blank=True)
	start_Date = models.DateField(help_text="Date the Partnership This Project Begins  (Same or different as project dates)")
	end_Date = models.DateField(help_text="Date the Partnership This Project Ends (Same or different as project dates)")
	key_contact_name_1 = models.CharField(max_length=100, default=None, blank=True)
	key_contact_email_1 = models.EmailField(max_length=100, default=None, blank=True)
	key_contact_name_2 = models.CharField(max_length=100, default=None, blank=True, help_text="(Optional)")
	key_contact_email_2 = models.EmailField(max_length=100, default=None, blank=True, help_text="(Optional)")
	partner_Budget =models.IntegerField()

	def __str__(self):
		return self.project_name

class Project_Donor(models.Model):
	donor_name = models.ForeignKey(Donor, on_delete=models.CASCADE)
	project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
	recruitment_source = models.CharField(max_length=200, help_text="How the donor was secured (e.g Funding Application, SCR, etc)")
	type_of_donation = models.CharField(max_length=200, help_text="Type contribution of the funder in the project")
	value_of_donation = models.CharField(max_length=200, help_text="Monetary value of contribution of the funder in the project")
	key_contact_name = models.CharField(max_length=200)
	key_contact_email = models.EmailField(max_length=200)

	def __str__(self):
		return self.project_name