from django.urls import path
from . import views

urlpatterns = [
    #urls for managing Hubs
    path('hub/add', views.organization_hub_add_view, name='organization_hub_add'),
    path('hub/list', views.organization_hub_list_view, name='organization_hub_list'),
    path('hub/<int:id>/detail', views.organization_hub_detail_view, name='organization_hub_detail'),
    path('hub/<int:id>/update', views.organization_hub_update_view, name='organization_hub_update'),
    path('hub/<int:id>/delete', views.organization_hub_delete_view, name='organization_hub_delete'),
    # urls for managing departments
    path('department/add', views.department_add_view, name='department_add'),
    path('department/list', views.department_list_view, name='department_list'),
    path('department/<int:id>/detail', views.department_detail_view, name='department_detail'),
    path('department/<int:id>/update', views.department_update_view, name='department_update'),
    path('department/<int:id>/delete', views.department_delete_view, name='department_delete'),
    # urls for managing Job Positions
    path('position/add', views.position_add_view, name='position_add'),
    path('position/list', views.position_list_view, name='position_list'),
    path('position/<int:id>/detail', views.position_detail_view, name='position_detail'),
    path('position/<int:id>/update', views.position_update_view, name='position_update'),
    path('position/<int:id>/delete', views.position_delete_view, name='position_delete'),
    path('ajax/load-hub-department/', views.ajax_load_hub_department, name='ajax_load_hub_department'),
    # urls for managing Users
    path('user/add', views.user_add_view, name='user_add'),
    path('user/list', views.user_list_view , name='user_list'),
    path('user/<int:id>/detail', views.user_detail_view, name='user_detail'),
    path('user/<int:id>/update', views.user_update_view, name='user_update'),
    # path('user/<int:id>/delete', views.user_delete_view, name='user_delete'),


 
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]
