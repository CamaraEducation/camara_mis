from django import forms
from accounts.models import Hub

from projects.models import Project
from .models import County_Region, District_Woreda, School, Sub_County_Zone

class DateInput(forms.DateInput):
    input_type = 'date'

class AddCountyRegionForm(forms.ModelForm):

    class Meta:
        model = County_Region
        fields = {'hub_name', 'county_or_region_name'}


class AddSubCountyZoneForm(forms.ModelForm):

    class Meta:
        model = Sub_County_Zone
        fields = {'county_or_region_name', 'sub_county_or_Zone_name'}


class AddDistrictWoredaForm(forms.ModelForm):

    class Meta:
        model = District_Woreda
        fields = {'county_or_region_name', 'sub_county_or_Zone_name', 'district_or_woreda_name'}

class AddSchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = {'school_code', 'country', 'school_name', 'school_level', 'school_ownership', 'school_area',
                    'po_box', 'phone_number_1', 'phone_number_2', 'website', 'female_teachers', 'male_teachers',
                    'female_students', 'male_students', 'female_sn_students', 'male_sn_students', 'county_or_region_name',
                    'sub_county_or_Zone_name', 'district_or_woreda_name', 'project_name'}

    def __init__(self, user, *args, **kwargs):
        super(AddSchoolForm, self).__init__(*args, **kwargs)
        self.fields['county_or_region_name'].queryset = County_Region.objects.filter(hub_name = user)
        self.fields['project_name'].queryset = Project.objects.filter(hub = user)
        self.fields['country'].queryset = Hub.objects.filter(hub_name = user)
        # self.fields['sub_county_or_Zone_name'].queryset = Sub_County_Zone.objects.none()


class UploadSchoolForm(forms.Form):
	school_upload = forms.FileField(required=True)