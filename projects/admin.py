from django.contrib import admin

# Register your models here.
from .models import Project, Partner, Donor, Project_Donor, Project_Partner

admin.site.register(Project)
admin.site.register(Partner)
admin.site.register(Donor)
admin.site.register(Project_Partner)
admin.site.register(Project_Donor)