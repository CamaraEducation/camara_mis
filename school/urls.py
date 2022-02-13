from django.urls import path
from . import views

urlpatterns = [
    #urls for managing school
    path('school/add', views.school_add_view, name='school_add'),
    path('school/list', views.school_list_view, name='school_list'),
    path('school/<int:id>/detail', views.school_detail_view, name='school_detail'),
    path('school/<int:id>/update', views.school_update_view, name='school_update'),
    path('school/<int:id>/delete', views.school_delete_view, name='school_delete'),
    path('school/upload/', views.school_upload_view, name='school_upload'),

    path('county_region/add', views.county_region_add_view, name='county_region_add'),
    path('county_region/list', views.county_region_list_view, name='county_region_list'),
    path('county_region/<int:id>/detail', views.county_region_detail_view, name='county_region_detail'),
    path('county_region/<int:id>/update', views.county_region_update_view, name='county_region_update'),
    path('county_region/<int:id>/delete', views.county_region_delete_view, name='county_region_delete'),

    path('sub_county_zone/add', views.sub_county_zone_add_view, name='sub_county_zone_add'),
    path('sub_county_zone/list', views.sub_county_zone_list_view, name='sub_county_zone_list'),
    path('sub_county_zone/<int:id>/detail', views.sub_county_zone_detail_view, name='sub_county_zone_detail'),
    path('sub_county_zone/<int:id>/update', views.sub_county_zone_update_view, name='sub_county_zone_update'),
    path('sub_county_zone/<int:id>/delete', views.sub_county_zone_delete_view, name='sub_county_zone_delete'),

    path('district_woreda/add', views.district_woreda_add_view, name='district_woreda_add'),
    path('district_woreda/list', views.district_woreda_list_view, name='district_woreda_list'),
    path('district_woreda/<int:id>/detail', views.district_woreda_detail_view, name='district_woreda_detail'),
    path('district_woreda/<int:id>/update', views.district_woreda_update_view, name='district_woreda_update'),
    path('district_woreda/<int:id>/delete', views.district_woreda_delete_view, name='district_woreda_delete'),
]
