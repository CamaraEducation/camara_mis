from django import forms
from .models import Course, Training, Training_Attendance

class DateInput(forms.DateInput):
    input_type = 'date'


class AddCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = {'hub', 'project', 'course_name', 'course_target', 'course_description', 'course_certificate',
                    'course_version', 'course_delivery', 'course_price', 'course_cost', 'course_designed_by',
                    'course_status',}

class AddTrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = {'training_name', 'course', 'instructor', 'number_of_participant', 'number_of_schools',
                    'start_date', 'end_date', 'training_location', 'status',}
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
    	}

class AddTrainingAttendanceForm(forms.ModelForm):

    class Meta:
        model = Training_Attendance
        fields = {'training', 'first_name', 'last_name', 'school', 'phone_number',
                    'email', 'subject_thought',}
