from django import forms
from .models import School

class DateInput(forms.DateInput):
    input_type = 'date'


class AddSchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = {'school_code', 'country', 'school_name', 'school_level', 'school_ownership', 'school_area',
                    'po_box', 'phone_number_1', 'phone_number_2', 'website', 'female_teachers', 'male_teachers',
                    'female_students', 'male_students', 'female_sn_students', 'male_sn_students', }
