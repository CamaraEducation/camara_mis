from django.db import models
from accounts.models import Hub, UserProfile
from .constants import CERTIFICATE_AVAILABLE_CHOICE, COURSE_DELIVERY_METHOD, COURSE_STATUS_CHOICES,TRAINING_STATUS_CHOICES
from projects.models import Project
from school.models import School
# Create your models here.

class Course(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE, help_text='The hub the course is designed for.')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,help_text='The project the course is designed for.')
    course_name = models.CharField(max_length=100, help_text='The name of the course')
    course_code = models.CharField(max_length=20, unique=True, help_text='Short code to identify the course (must be unique).')
    course_target = models.CharField(max_length=100, help_text="The target group of the course")
    course_description = models.CharField(max_length=250, help_text='Short course description')
    course_certificate = models.CharField(max_length=10, choices=CERTIFICATE_AVAILABLE_CHOICE, default='Yes')
    course_version = models.CharField(max_length=20, default=None, blank=True)
    course_delivery = models.CharField(max_length=20, choices=COURSE_DELIVERY_METHOD)
    course_duration = models.IntegerField(help_text='Estimated course duration in hours.')
    course_price = models.CharField(max_length=20, default=None, blank=True)
    course_cost = models.CharField(max_length=20, default=None, blank=True)
    course_designed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_status = models.CharField(max_length=20, choices=COURSE_STATUS_CHOICES)

    def __str__(self):
        return self.course_name

class Training(models.Model):
    training_name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    number_of_participant = models.IntegerField()
    number_of_schools = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    traing_duration = models.IntegerField(help_text='The training duration in hours.')
    training_location = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=TRAINING_STATUS_CHOICES)

    def __str__(self):
        return self.training_name

class Training_Attendance(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=15)
    email = models.EmailField(blank=True, default=None, null=True)
    subject_thought = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name