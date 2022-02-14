from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AddCourseForm, AddTrainingAttendanceForm, AddTrainingForm
from training.models import Course, Training, Training_Attendance

###################### Views for managing course ######################
def course_list_view(request):
    user = request.user.userprofile.hub
    courses_list = Course.objects.all().filter(hub=user)
    context = {
		'title': 'course List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'course_nav_link_active': 'active',
		'courses_list': courses_list
	}
    return render(request, 'courses/course_list.html', context)

def course_add_view(request):
    course_add_form = AddCourseForm(request.POST or None)
    if course_add_form.is_valid():
        course_add_form.save()
        messages.success(request, "course added successfully")
        return redirect('course_list')
    context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'course_nav_link_active': 'active',
		'title':'Add A course',
		'course_add_form':course_add_form,
	}
    return render(request, 'courses/course_add.html', context)

def course_detail_view(request, id=id):
	obj = get_object_or_404(Course, id=id)
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'course_nav_link_active': 'active',
		'title':'course Detial',
		'obj':obj,
	}
	return render(request, 'courses/course_detail.html', context)

def course_update_view(request, id=id):
	obj = get_object_or_404(Course, id=id)
	course_update_form = AddCourseForm(request.POST or None, instance=obj)
	if course_update_form.is_valid():
		course_update_form.save()
		messages.success(request, "course Updated successfully")
		return redirect('course_list')
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'course_nav_link_active': 'active',
		'title':'Update course',
		'course_update_form':course_update_form,
	}
	return render(request, 'courses/course_update.html', context)

def course_delete_view(request, id=id):
	obj = get_object_or_404(Course, id=id)
	obj.delete()
	messages.success(request, "course Deleted successfully")
	return redirect('course_list')

###################### End Views for managing course ######################

###################### Views for managing training ######################
def training_list_view(request):
    trainings_list = Training.objects.all()
    context = {
		'title': 'training List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_nav_link_active': 'active',
		'trainings_list': trainings_list
	}
    return render(request, 'trainings/training_list.html', context)

def training_add_view(request):
    training_add_form = AddTrainingForm(request.POST or None)
    if training_add_form.is_valid():
        training_add_form.save()
        messages.success(request, "training added successfully")
        return redirect('training_list')
    context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_nav_link_active': 'active',
		'title':'Add A training',
		'training_add_form':training_add_form,
	}
    return render(request, 'trainings/training_add.html', context)

def training_detail_view(request, id=id):
	obj = get_object_or_404(Training, id=id)
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_nav_link_active': 'active',
		'title':'training Detial',
		'obj':obj,
	}
	return render(request, 'trainings/training_detail.html', context)

def training_update_view(request, id=id):
	obj = get_object_or_404(Training, id=id)
	training_update_form = AddTrainingForm(request.POST or None, instance=obj)
	if training_update_form.is_valid():
		training_update_form.save()
		messages.success(request, "training Updated successfully")
		return redirect('training_list')
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_nav_link_active': 'active',
		'title':'Update training',
		'training_update_form':training_update_form,
	}
	return render(request, 'trainings/training_update.html', context)

def training_delete_view(request, id=id):
	obj = get_object_or_404(Training, id=id)
	obj.delete()
	messages.success(request, "training Deleted successfully")
	return redirect('training_list')

###################### End Views for managing training ######################

###################### Views for managing training_attendance ######################
def training_attendance_list_view(request):
    training_attendances_list = Training_Attendance.objects.all()
    context = {
		'title': 'training_attendance List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_attendance_nav_link_active': 'active',
		'training_attendances_list': training_attendances_list
	}
    return render(request, 'training_attendances/training_attendance_list.html', context)

def training_attendance_add_view(request):
    training_attendance_add_form = AddTrainingAttendanceForm(request.POST or None)
    if training_attendance_add_form.is_valid():
        training_attendance_add_form.save()
        messages.success(request, "training_attendance added successfully")
        return redirect('training_attendance_list')
    context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_attendance_nav_link_active': 'active',
		'title':'Add A training_attendance',
		'training_attendance_add_form':training_attendance_add_form,
	}
    return render(request, 'training_attendances/training_attendance_add.html', context)

def training_attendance_detail_view(request, id=id):
	obj = get_object_or_404(Training_Attendance, id=id)
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_attendance_nav_link_active': 'active',
		'title':'training_attendance Detial',
		'obj':obj,
	}
	return render(request, 'training_attendances/training_attendance_detail.html', context)

def training_attendance_update_view(request, id=id):
	obj = get_object_or_404(Training_Attendance, id=id)
	training_attendance_update_form = AddTrainingAttendanceForm(request.POST or None, instance=obj)
	if training_attendance_update_form.is_valid():
		training_attendance_update_form.save()
		messages.success(request, "training_attendance Updated successfully")
		return redirect('training_attendance_list')
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'training_attendance_nav_link_active': 'active',
		'title':'Update training_attendance',
		'training_attendance_update_form':training_attendance_update_form,
	}
	return render(request, 'training_attendances/training_attendance_update.html', context)

def training_attendance_delete_view(request, id=id):
	obj = get_object_or_404(Training_Attendance, id=id)
	obj.delete()
	messages.success(request, "training_attendance Deleted successfully")
	return redirect('training_attendance_list')

###################### End Views for managing training_attendance ######################