from django import forms

from accounts.models import Hub
from .models import Monitor, Operating_System, Operating_system_Version, Supplier, Computer

class DateInput(forms.DateInput):
    input_type = 'date'

class AddSuplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('name', 'description', 'address', 'contact', 'contact_2', 'contact_person', 'payment_mode',
                    'supplier_email', 'supplier_email_2', 'supplier_website', 'supplier_category', 'supplier_items', 'supplier_items_status')
        labels = {
            'name':'Supplier Name',
            'contact': 'Supplier Phone Number',
            'contact_2': 'Additional Phone Number',
            'supplier_email_2': 'Additional Email'
        }

class AddComputerForm(forms.ModelForm):
    c_affritrack_number = forms.CharField(label = "Computer Affritrack Number")

    class Meta:
        model = Computer
        fields = ('hub', 'c_affritrack_number', 'serial_number', 'brand', 'model', 'donor_id',
                    'container_number', 'device_status', 'supplier', 'processor_type', 
                    'processor_speed', 'memory_type', 'memory_size', 'storage_type', 
                    'storage_size', 'os_type', 'os_version', 'working_status', 'date_received', 'comment')
        widgets = {
            'date_received': DateInput(),
            'c_affritrack_number': forms.TextInput(attrs={'required':True})
        }

    def __init__(self, user, *args, **kwargs):
        super(AddComputerForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.filter(hub_name = user)

class UpdateComputerForm(forms.ModelForm):
    c_affritrack_number = forms.CharField(label = "Computer Affritrack Number")

    class Meta:
        model = Computer
        fields = ('hub', 'c_affritrack_number', 'serial_number', 'brand', 'model', 'donor_id',
                    'container_number', 'device_status', 'supplier', 'processor_type', 
                    'processor_speed', 'memory_type', 'memory_size', 'storage_type', 
                    'storage_size', 'os_type', 'os_version', 'working_status', 'comment')
        widgets = {
            'c_affritrack_number': forms.TextInput(attrs={'required':True})
        }
    def __init__(self, user, request, *args, **kwargs):
        super(UpdateComputerForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.filter(hub_name = user)
        if not request.user.is_staff:
            self.fields['hub'].disabled = True
            self.fields['c_affritrack_number'].disabled = True
            self.fields['serial_number'].disabled = True
            self.fields['container_number'].disabled = True
        elif request.user.is_superuser:
            self.fields['hub'].disabled = False
            self.fields['c_affritrack_number'].disabled = False
            self.fields['serial_number'].disabled = False


class AddMonitorForm(forms.ModelForm):
    m_affritrack_number = forms.CharField(label = "Monitor Affritrack Number", required=True)

    class Meta:
        model = Monitor
        fields = ('hub','m_affritrack_number', 'serial_number', 'brand', 'donor_id', 'container_number',
                    'device_status', 'supplier', 'date_received', 'screen_size', 'working_status', 'comment')
        widgets = {
            'date_received': DateInput()
        }

    def __init__(self, user, *args, **kwargs):
        super(AddMonitorForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.filter(hub_name = user)

class UpdateMonitorForm(forms.ModelForm):
    m_affritrack_number = forms.CharField(label = "Monitor Affritrack Number", required=True)

    class Meta:
        model = Monitor
        fields = ('hub','m_affritrack_number', 'serial_number', 'brand', 'donor_id', 'container_number',
                    'device_status', 'supplier', 'screen_size', 'working_status', 'comment')

    def __init__(self, user, request, *args, **kwargs):
        super(UpdateMonitorForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.filter(hub_name = user)
        if not request.user.is_staff:
            self.fields['hub'].disabled = True
            self.fields['m_affritrack_number'].disabled = True
            self.fields['serial_number'].disabled = True
            self.fields['container_number'].disabled = True
        elif request.user.is_superuser:
            self.fields['hub'].disabled = False
            self.fields['m_affritrack_number'].disabled = False
            self.fields['serial_number'].disabled = False
            self.fields['container_number'].disabled = False

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