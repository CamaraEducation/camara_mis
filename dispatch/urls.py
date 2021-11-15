from django.urls import path
from . import views


app_name = 'dispatch'
urlpatterns = [
    #urls for managing Applicant
    path('applicant/add', views.applicant_add_view, name='applicant_add'),
    path('applicant/list', views.applicant_list_view, name='applicant_list'),
    path('applicant/<int:id>/detail', views.applicant_detail_view, name='applicant_detail'),
    path('applicant/<int:id>/update', views.applicant_update_view, name='applicant_update'),
    path('applicant/<int:id>/delete', views.applicant_delete_view, name='applicant_delete'),
    # path('ajax/load-school/', views.ajax_load_school, name='ajax_load_school'),

    #urls for managing computer Request 
    path('school_computer_request/<int:id>/add', views.school_computer_request_add, name='school_computer_request_add'),
    path('computer_request/add', views.computer_request_add_view, name='computer_request_add'),
    path('computer_request/list', views.computer_request_list_view, name='computer_request_list'),
    path('computer_request/<int:id>/detail', views.computer_request_detail_view, name='computer_request_detail'),
    path('computer_request/<int:id>/update', views.computer_request_update_view, name='computer_request_update'),
    path('computer_request/<int:id>/delete', views.computer_request_delete_view, name='computer_request_delete'),

    path('computer_request_dispatch_process/<int:id>/dispatch', views.computer_request_dispatch_process_view, name='computer_request_dispatch_process'),
    path('dispacth/ajax/check_status', views.product_status_check, name='check_status'),
]