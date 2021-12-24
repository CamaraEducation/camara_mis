from django import forms
from .models import Monitor, Operating_System, Operating_system_Version, Supplier, Computer

class DateInput(forms.DateInput):
    input_type = 'date'

class AddSuplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('name', 'description', 'address', 'contact', 'contact_person', 'payment_mode')

class AddComputerForm(forms.ModelForm):
    c_affritrack_number = forms.CharField(label = "Computer Affritrack Number")

    class Meta:
        model = Computer
        fields = ('hub', 'c_affritrack_number', 'serial_number', 'brand', 'model', 'donor_id',
                    'container_number', 'device_status', 'supplier', 'processor_type', 
                    'processor_speed', 'memory_type', 'memory_size', 'storage_type', 
                    'storage_size', 'os_type', 'os_version', 'working_status', 'date_received', 'comment')
        widgets = {
            'date_received': DateInput()
        }

class UpdateComputerForm(forms.ModelForm):
    c_affritrack_number = forms.CharField(label = "Computer Affritrack Number")

    class Meta:
        model = Computer
        fields = ('hub', 'c_affritrack_number', 'serial_number', 'brand', 'model', 'donor_id',
                    'container_number', 'device_status', 'supplier', 'processor_type', 
                    'processor_speed', 'memory_type', 'memory_size', 'storage_type', 
                    'storage_size', 'os_type', 'os_version', 'working_status', 'comment')
        widgets = {
            'date_received': DateInput()
        }


class AddMonitorForm(forms.ModelForm):
    m_affritrack_number = forms.CharField(label = "Monitor Affritrack Number")

    class Meta:
        model = Monitor
        fields = ('hub','m_affritrack_number', 'serial_number', 'brand', 'donor_id', 'container_number',
                    'device_status', 'supplier', 'date_received', 'screen_size', 'working_status', 'comment')
        widgets = {
            'date_received': DateInput()
        }


class UploadComputerForm(forms.Form):
	computer_upload = forms.FileField()

class UploadMonitorForm(forms.Form):
	monitor_upload = forms.FileField()

class AddOSForm(forms.ModelForm):

    class Meta:
        model = Operating_System
        fields = ('os_name',)

class AddOSVForm(forms.ModelForm):

    class Meta:
        model = Operating_system_Version
        fields = ('os_name','os_version',)