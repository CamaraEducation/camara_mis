from django import forms
from django.db.models import fields
from .models import Computer_Applicant, Computer_Request, Dispatch

from school.models import School

class DateInput(forms.DateInput):
    input_type = 'date'


class AddComputerApplicantForm(forms.ModelForm):

    class Meta:
        model = Computer_Applicant
        fields = {'hub', 'school_name', 'full_name', 'email', 'phone_number',}

class AddComputerRequestForm(forms.ModelForm):

    class Meta:
        model = Computer_Request
        fields = {'hub', 'school_name', 'number_of_computers', 'applicant_id'}


class DispatchComputerForm(forms.ModelForm):

    class Meta:
        model = Dispatch
        fields = {'hub','computer_request_id', 'applicant_name', 'school_name',
                    'date_dispatched', 'dispatched_by', 'warranty_end'}


        widgets = {
            'date_dispatched': DateInput(),
            'warranty_end': DateInput()
        }

