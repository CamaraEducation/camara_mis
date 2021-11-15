from django.contrib import admin
from django.urls import path, include
from dashboard import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('products/', include('products.urls')),
    path('schools/', include('school.urls')),
    path('trainings/', include('training.urls')),
    path('dispatch/', include('dispatch.urls')),
    path('', views.home_view, name='home')
]
