from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('computer/report', views.computer_dashboard_view, name='computer_dashboard'),

]