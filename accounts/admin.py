from django.contrib import admin

# Register your models here.
from .models import Hub, Department, Position, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','hub','department', 'position', 'user_personal_email')
    # search_fields = ('user','hub','department', 'position', 'user_personal_email')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Hub)
admin.site.register(Department)
admin.site.register(Position)