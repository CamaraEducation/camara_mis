from django.contrib import admin
from django.urls import path, include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('products/', include('products.urls')),
    path('schools/', include('school.urls')),
    path('trainings/', include('training.urls')),
    path('', views.home_view, name='home')
]
