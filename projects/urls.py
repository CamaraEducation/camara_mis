from django.urls import path
from . import views

urlpatterns = [
    #urls for managing Project
    path('project/add', views.project_add_view, name='project_add'),
    path('project/list', views.project_list_view, name='project_list'),
    path('project/<int:id>/detail', views.project_detail_view, name='project_detail'),
    path('project/<int:id>/update', views.project_update_view, name='project_update'),
    path('project/<int:id>/delete', views.project_delete_view, name='project_delete'),

    #urls for managing Donor
    path('donor/add', views.donor_add_view, name='donor_add'),
    path('donor/list', views.donor_list_view, name='donor_list'),
    path('donor/<int:id>/detail', views.donor_detail_view, name='donor_detail'),
    path('donor/<int:id>/update', views.donor_update_view, name='donor_update'),
    path('donor/<int:id>/delete', views.donor_delete_view, name='donor_delete'),

    #urls for managing Donor
    path('partner/add', views.partner_add_view, name='partner_add'),
    path('partner/list', views.partner_list_view, name='partner_list'),
    path('partner/<int:id>/detail', views.partner_detail_view, name='partner_detail'),
    path('partner/<int:id>/update', views.partner_update_view, name='partner_update'),
    path('partner/<int:id>/delete', views.partner_delete_view, name='partner_delete'),

    #urls for managing project partner
    path('project_partner/add', views.project_partner_add_view, name='project_partner_add'),
    path('project_partner/list', views.project_partner_list_view, name='project_partner_list'),
    path('project_partner/<int:id>/detail', views.project_partner_detail_view, name='project_partner_detail'),
    path('project_partner/<int:id>/update', views.project_partner_update_view, name='project_partner_update'),
    path('project_partner/<int:id>/delete', views.project_partner_delete_view, name='project_partner_delete'),

    #urls for managing project Donor
    path('project_donor/add', views.project_donor_add_view, name='project_donor_add'),
    path('project_donor/list', views.project_donor_list_view, name='project_donor_list'),
    path('project_donor/<int:id>/detail', views.project_donor_detail_view, name='project_donor_detail'),
    path('project_donor/<int:id>/update', views.project_donor_update_view, name='project_donor_update'),
    path('project_donor/<int:id>/delete', views.project_donor_delete_view, name='project_donor_delete'),
]