from django.urls import path
from . import views

urlpatterns = [
    #urls for managing Supplier
    path('supplier/add', views.supplier_add_view, name='supplier_add'),
    path('supplier/list', views.supplier_list_view, name='supplier_list'),
    path('supplier/<int:id>/detail', views.supplier_detail_view, name='supplier_detail'),
    path('supplier/<int:id>/update', views.supplier_update_view, name='supplier_update'),
    path('supplier/<int:id>/delete', views.supplier_delete_view, name='supplier_delete'),

    #urls for managing Computers
    path('computer/add', views.computer_add_view, name='computer_add'),
    path('computer/list', views.computer_list_view, name='computer_list'),
    path('computer/<int:id>/detail', views.computer_detail_view, name='computer_detail'),
    path('computer/<int:id>/update', views.computer_update_view, name='computer_update'),
    path('computer/<int:id>/delete', views.computer_delete_view, name='computer_delete'),
    path('computer/upload/', views.computer_upload_view, name='computer_upload'),

    #urls for managing Monitor
    path('monitor/add', views.monitor_add_view, name='monitor_add'),
    path('monitor/list', views.monitor_list_view, name='monitor_list'),
    path('monitor/<int:id>/detail', views.monitor_detail_view, name='monitor_detail'),
    path('monitor/<int:id>/update', views.monitor_update_view, name='monitor_update'),
    path('monitor/<int:id>/delete', views.monitor_delete_view, name='monitor_delete'),
    path('monitor/upload/', views.monitor_upload_view, name='monitor_upload'),

    #urls for managing OS
    path('os/add', views.os_add_view, name='os_add'),
    path('os/list', views.os_list_view, name='os_list'),
    path('os/<int:id>/detail', views.os_detail_view, name='os_detail'),
    path('os/<int:id>/update', views.os_update_view, name='os_update'),
    path('os/<int:id>/delete', views.os_delete_view, name='os_delete'),

    #urls for managing OSV
    path('osv/add', views.osv_add_view, name='osv_add'),
    path('osv/list', views.osv_list_view, name='osv_list'),
    path('osv/<int:id>/detail', views.osv_detail_view, name='osv_detail'),
    path('osv/<int:id>/update', views.osv_update_view, name='osv_update'),
    path('osv/<int:id>/delete', views.osv_delete_view, name='osv_delete'),
    path('ajax/load-os-version/', views.ajax_load_os_version, name='ajax_load_os_version'),
]