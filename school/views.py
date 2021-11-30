import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import Hub
from .forms import AddSchoolForm, UploadSchoolForm
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

def school_upload_view(request):
	school_upload_form = UploadSchoolForm()
	hubs = Hub.objects.all()
	if request.method == 'POST':
		try:
			csv_file = request.FILES['school_upload']
			get_hub = request.POST.get("hub")
			hub = get_object_or_404(Hub, id=get_hub)
			if not csv_file.name.endswith('.csv'):
				messages.error(request, 'This is not a CSV file')

			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			next(io_string)
			for column in csv.reader(io_string, delimiter=',', quotechar='|'):
				_, created = School.objects.update_or_create(
					country=hub,
					school_code=column[0],
					school_name=column[1],
					school_level=column[2],
					school_ownership=column[3],
					school_area=column[4],
					po_box=column[5],
					phone_number_1=column[6],
					phone_number_2=column[7],
					email=column[8],
					website=column[9],
					female_teachers=column[10],
					male_teachers=column[11],
					female_students=column[12],
					male_students=column[13],
					female_sn_students=column[14],
					male_sn_students=column[15],
					)

			messages.success(request,f'The schools has been uploaded successfully!')
			return redirect('school_list')
		# except:
		# 	messages.error(request, 'Please Check your file it looks like you have duplicated items in you file or with the database')
		except Exception as e:
			print (e)
	context = {
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'title':'School Upload',
		'school_upload_form':school_upload_form,
		'hubs':hubs,
	}
	return render(request, 'schools/school_upload.html', context)
###################### End Views for managing school ######################
