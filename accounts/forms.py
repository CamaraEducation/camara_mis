from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hub, Department, Position, UserProfile


class DateInput(forms.DateInput):
    input_type = 'date'

class AddOrganizationHubForm(forms.ModelForm):

	class Meta:
		model = Hub
		fields = ('hub_code', 'hub_name', 'hub_located_country', 'hub_address', 
			'hub_email', 'hub_phone', 'hub_registration_year', 'hub_registration_number',
			'hub_registration_status', 'hub_tin_number', 'hub_country_director',
			'hub_website', 'hub_facebook', 'hub_twitter', 'hub_instagram', 'hub_linkedin', 'hub_youtube', )

		widgets = {
        'hub_registration_year': DateInput()
    	}

class AddDepartmentForm(forms.ModelForm):

	class Meta:
		model = Department
		fields = ('hub', 'department_code', 'department_name', 'department_email', 'department_manager', 'department_phone_number', 'department_role',)

class AddPositionForm(forms.ModelForm):

	class Meta:
		model = Position
		fields = ('hub', 'department', 'position_name', 'position_description',)
		labels = {
			'hub': 'Hub Name',
			'department': 'Department Name',
			'position_name': 'Position Name',
			'position_description': 'Position Discriprtion',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['department'].queryset = Department.objects.none()

		if 'hub' in self.data:
			try:
				hub_id = int(self.data.get('hub'))
				self.fields['department'].queryset = Department.objects.filter(hub_id=hub_id).order_by('department_name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['department'].queryset = self.instance.hub.department_set.order_by('department_name')

class AddUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2')

class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ('username','first_name','last_name')

class AddUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('hub', 'department', 'position','user_code','user_personal_email', 'user_hired_date', 'user_employement_type',
			'user_gender', 'user_phone_number', 'user_education_level', 'user_birth_date', 'user_contact_name',
			'user_contact_phone_number', 'user_contact_email', 'user_contact_relationship', 'user_contact_address')
		labels = {
			'hub': 'Hub Name',
			'department': 'Department Name',
			'position_name': 'Position Name',
			'user_personal_email': 'Camara Email'
		}
		widgets = {
        'user_birth_date': DateInput(),
        'user_hired_date': DateInput()
    	}

	def __init__(self, *args, **kwargs):
		super(AddUserProfileForm, self).__init__(*args, **kwargs)
		self.fields['department'].queryset = Department.objects.none()
		self.fields['position'].queryset = Position.objects.none()

		if 'hub' in self.data:
			try:
				hub_id = int(self.data.get('hub'))
				self.fields['department'].queryset = Department.objects.filter(hub_id=hub_id).order_by('department_name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['department'].queryset = self.instance.hub.department_set.order_by('department_name')

		if 'department' in self.data:
			try:
				department_id = int(self.data.get('department'))
				self.fields['position'].queryset = Position.objects.filter(department_id=department_id).order_by('position_name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['position'].queryset = self.instance.department.position_set.order_by('position_name')
