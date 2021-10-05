from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import AddSchoolForm
from .models import School

###################### Views for managing school ######################
def school_list_view(request):
    schools_list = School.objects.all()
    context = {
		'title': 'school List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'schools_list': schools_list
	}
    return render(request, 'schools/school_list.html', context)

def school_add_view(request):
    school_add_form = AddSchoolForm(request.POST or None)
    if school_add_form.is_valid():
        school_add_form.save()
        messages.success(request, "School added successfully")
        return redirect('school_list')
    context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'title':'Add A school',
		'school_add_form':school_add_form,
	}
    return render(request, 'schools/school_add.html', context)

def school_detail_view(request, id=id):
	obj = get_object_or_404(School, id=id)
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'title':'school Detial',
		'obj':obj,
	}
	return render(request, 'schools/school_detail.html', context)

def school_update_view(request, id=id):
	obj = get_object_or_404(School, id=id)
	school_update_form = AddSchoolForm(request.POST or None, instance=obj)
	if school_update_form.is_valid():
		school_update_form.save()
		messages.success(request, "School Updated successfully")
		return redirect('school_list')
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'title':'Update school',
		'school_update_form':school_update_form,
	}
	return render(request, 'schools/school_update.html', context)

def school_delete_view(request, id=id):
	obj = get_object_or_404(school, id=id)
	obj.delete()
	messages.success(request, "School Deleted successfully")
	return redirect('school_list')

###################### End Views for managing school ######################
