from django.urls import path
from . import views

urlpatterns = [
    #urls for managing course
    path('course/add', views.course_add_view, name='course_add'),
    path('course/list', views.course_list_view, name='course_list'),
    path('course/<int:id>/detail', views.course_detail_view, name='course_detail'),
    path('course/<int:id>/update', views.course_update_view, name='course_update'),
    path('course/<int:id>/delete', views.course_delete_view, name='course_delete'),

    #urls for managing training
    path('training/add', views.training_add_view, name='training_add'),
    path('training/list', views.training_list_view, name='training_list'),
    path('training/<int:id>/detail', views.training_detail_view, name='training_detail'),
    path('training/<int:id>/update', views.training_update_view, name='training_update'),
    path('training/<int:id>/delete', views.training_delete_view, name='training_delete'),

    #urls for managing training_attendance
    path('training_attendance/add', views.training_attendance_add_view, name='training_attendance_add'),
    path('training_attendance/list', views.training_attendance_list_view, name='training_attendance_list'),
    path('training_attendance/<int:id>/detail', views.training_attendance_detail_view, name='training_attendance_detail'),
    path('training_attendance/<int:id>/update', views.training_attendance_update_view, name='training_attendance_update'),
    path('training_attendance/<int:id>/delete', views.training_attendance_delete_view, name='training_attendance_delete'),
]