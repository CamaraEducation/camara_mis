from django import forms
from django.db import models
from django.db.models import fields

from .models import Donor, Partner, Project, Project_Partner, Project_Donor
from accounts.models import Hub

class DateInput(forms.DateInput):
    input_type = 'date'

class AddProjectForm(forms.ModelForm):

	project_description = forms.CharField(required=True)

	class Meta:
		model = Project
		fields = ('hub', 'project_code', 'project_name', 'project_description', 'project_budget', 'project_manager', 'project_start_date', 'project_end_date')

		widgets = {
        'project_start_date': DateInput(),
        'project_end_date': DateInput()
    	}

class AddDonorForm(forms.ModelForm):


	class Meta:
		model = Donor
		fields = {'donor_name', 'donor_description', 'donor_website', 'donor_dates', 'donor_email',
					'country', 'donor_contact', 'donation_range', 'donation_category',
					'donor_type', 'key_contact_name', 'key_contact_email', }

		widgets = {
        'donor_dates': DateInput()
    	}

class AddPartnerForm(forms.ModelForm):

	class Meta:
		model = Partner
		fields = {'partner_name', 'partner_adress', 'partner_country', 'key_contact_name', 'key_contact_email',
					'partner_website', 'partner_description', 'partnership_start',	'areas_of_patnership' }
		widgets = {
        'partnership_start': DateInput()
    	}

class AddProjectPartnerForm(forms.ModelForm):

	class Meta:
		model = Project_Partner
		fields = {"project_name", "partner_name", "partner_role", "start_Date", "end_Date", "key_contact_name_1", 
					"key_contact_email_1", "key_contact_name_2", "key_contact_email_2", "partner_Budget"}
		widgets = {
        'start_Date': DateInput(),
		'end_Date': DateInput()
    	}

class AddProjectDonorForm(forms.ModelForm):

	class Meta:
		model = Project_Donor
		fields = {"donor_name", "project_name", "recruitment_source", "type_of_donation", "value_of_donation", 
					"key_contact_name", "key_contact_email"}

