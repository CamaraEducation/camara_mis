from django.urls import path
from . import views

urlpatterns = [
    #urls for managing school
    path('school/add', views.school_add_view, name='school_add'),
    path('school/list', views.school_list_view, name='school_list'),
    path('school/<int:id>/detail', views.school_detail_view, name='school_detail'),
    path('school/<int:id>/update', views.school_update_view, name='school_update'),
    path('school/<int:id>/delete', views.school_delete_view, name='school_delete'),
]