import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import Hub
from projects.models import Project
from .forms import AddSchoolForm, UploadSchoolForm, AddCountyRegionForm, AddSubCountyZoneForm, AddDistrictWoredaForm
from .models import School, County_Region, Sub_County_Zone, District_Woreda

###################### Views for managing school ######################
def school_list_view(request):
    user = request.user.userprofile.hub
    schools_list = School.objects.all().filter(country=user)
    context = {
		'title': 'school List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'school_nav_link_active': 'active',
		'schools_list': schools_list
	}
    return render(request, 'schools/school_list.html', context)

def school_add_view(request):
    user = request.user.userprofile.hub
    school_add_form = AddSchoolForm(user, request.POST or None)
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
	user = request.user.userprofile.hub
	obj = get_object_or_404(School, id=id)
	school_update_form = AddSchoolForm(user, request.POST or None, instance=obj)
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
	obj = get_object_or_404(School, id=id)
	obj.delete()
	messages.success(request, "School Deleted successfully")
	return redirect('school_list')

def school_upload_view(request):
	school_upload_form = UploadSchoolForm()
	user = request.user.userprofile.hub
	projects = Project.objects.all().filter(hub = user)
	county_regions = County_Region.objects.all().filter(hub_name=user)
	if request.method == 'POST':
		try:
			csv_file = request.FILES['school_upload']
			project_selected = get_object_or_404(Project, id = request.POST.get("project"))
			county_region_selected = get_object_or_404(County_Region, id = request.POST.get("county_region"))
			sub_county_zone_selected = get_object_or_404(Sub_County_Zone, id = request.POST.get("sub_county_zone"))
			if not csv_file.name.endswith('.csv'):
				messages.error(request, 'This is not a CSV file')

			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			next(io_string)
			for column in csv.reader(io_string, delimiter=',', quotechar='|'):
				_, created = School.objects.update_or_create(
					country=user,
					project_name = project_selected,
					county_or_region_name = county_region_selected,
					sub_county_or_Zone_name=sub_county_zone_selected,
					school_code=column[0],
					school_name=column[1],
					school_level=column[2],
					school_ownership=column[3],
					school_area=column[4],
					district_or_woreda_name=column[5],
					po_box=column[6],
					phone_number_1=column[7],
					phone_number_2=column[8],
					email=column[9],
					website=column[10],
					female_teachers=column[11],
					male_teachers=column[12],
					female_students=column[13],
					male_students=column[14],
					female_sn_students=column[15],
					male_sn_students=column[16],
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
		'projects':projects,
		'county_regions': county_regions,
	}
	return render(request, 'schools/school_upload.html', context)

def ajax_load_sub_county_zone(request):
	if request.GET.get('county_id'):
		county_id = request.GET.get('county_id')
		sub_county_zones = Sub_County_Zone.objects.filter(county_or_region_name=county_id)
		return render(request, 'schools/sub_county_zone_dropdown_option.html', {'sub_county_zones': sub_county_zones})
###################### End Views for managing school ######################

###################### Views for managing Counties/Regions ######################
def county_region_list_view(request):
    county_region_list = County_Region.objects.all()
    context = {
		'title': 'County/Region List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'county_region_nav_link_active': 'active',
		'county_region_list': county_region_list
	}
    return render(request, 'county_regions/county_region_list.html', context)

def county_region_add_view(request):
    user = request.user.userprofile.hub
    county_region_add_form = AddCountyRegionForm(user, request.POST or None)
    if county_region_add_form.is_valid():
        county_region_add_form.save()
        messages.success(request, "County/Region has been added successfully")
        return redirect('county_region_list')
    context = {
		'title': 'County/Region Add',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'county_region_nav_link_active': 'active',
		'county_region_add_form':county_region_add_form,
	}
    return render(request, 'county_regions/county_region_add.html', context)

def county_region_detail_view(request, id=id):
	obj = get_object_or_404(County_Region, id=id)
	context = {
		'title': 'County/Region Detail',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'county_region_nav_link_active': 'active',
		'obj':obj,
	}
	return render(request, 'county_regions/county_region_detail.html', context)

def county_region_update_view(request, id=id):
	obj = get_object_or_404(County_Region, id=id)
	county_region_update_form = AddCountyRegionForm(request.POST or None, instance=obj)
	if county_region_update_form.is_valid():
		county_region_update_form.save()
		messages.success(request, "County/Region has been Updated successfully")
		return redirect('county_region_list')
	context = {
		'title': 'County/Region Update',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'county_region_nav_link_active': 'active',
		'county_region_update_form':county_region_update_form,
	}
	return render(request, 'county_regions/county_region_update.html', context)

def county_region_delete_view(request, id=id):
	obj = get_object_or_404(County_Region, id=id)
	obj.delete()
	messages.success(request, "County/Region has been Deleted successfully")
	return redirect('county_region_list')
###################### End Views for managing Counties/Regions ######################

###################### Views for managing Sub-Counties/Zone ######################
def sub_county_zone_list_view(request):
    sub_county_zone_list = Sub_County_Zone.objects.all()
    context = {
		'title': 'Sub County/Zone List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'sub_county_zone_nav_link_active': 'active',
		'sub_county_zone_list': sub_county_zone_list
	}
    return render(request, 'sub_county_zones/sub_county_zone_list.html', context)

def sub_county_zone_add_view(request):
    sub_county_zone_add_form = AddSubCountyZoneForm(request.POST or None)
    if sub_county_zone_add_form.is_valid():
        sub_county_zone_add_form.save()
        messages.success(request, "Sub County/Zone has been added successfully")
        return redirect('sub_county_zone_list')
    context = {
		'title': 'Sub County/Zone Add',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'sub_county_zone_nav_link_active': 'active',
		'sub_county_zone_add_form':sub_county_zone_add_form,
	}
    return render(request, 'sub_county_zones/sub_county_zone_add.html', context)

def sub_county_zone_detail_view(request, id=id):
	obj = get_object_or_404(Sub_County_Zone, id=id)
	context = {
		'title': 'Sub County/Zone Detail',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'sub_county_zone_nav_link_active': 'active',
		'obj':obj,
	}
	return render(request, 'sub_county_zones/sub_county_zone_detail.html', context)

def sub_county_zone_update_view(request, id=id):
	obj = get_object_or_404(Sub_County_Zone, id=id)
	sub_county_zone_update_form = AddSubCountyZoneForm(request.POST or None, instance=obj)
	if sub_county_zone_update_form.is_valid():
		sub_county_zone_update_form.save()
		messages.success(request, "Sub County/Zone has been Updated successfully")
		return redirect('sub_county_zone_list')
	context = {
		'title': 'Sub County/Zone Update',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'sub_county_zone_nav_link_active': 'active',
		'sub_county_zone_update_form':sub_county_zone_update_form,
	}
	return render(request, 'sub_county_zones/sub_county_zone_update.html', context)

def sub_county_zone_delete_view(request, id=id):
	obj = get_object_or_404(Sub_County_Zone, id=id)
	obj.delete()
	messages.success(request, "Sub County/Zone has been Deleted successfully")
	return redirect('sub_county_zone_list')
###################### End Views for managing Sub-Counties/Zone ######################

###################### Views for managing District/Woreda ######################
def district_woreda_list_view(request):
    district_woreda_list = District_Woreda.objects.all()
    context = {
		'title': 'District/Woreda List',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'district_woreda_nav_link_active': 'active',
		'district_woreda_list': district_woreda_list
	}
    return render(request, 'district_woredas/district_woreda_list.html', context)

def district_woreda_add_view(request):
    district_woreda_add_form = AddDistrictWoredaForm(request.POST or None)
    if district_woreda_add_form.is_valid():
        district_woreda_add_form.save()
        messages.success(request, "District/Woreda has been added successfully")
        return redirect('district_woreda_list')
    context = {
		'title': 'District/Woreda Add',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'district_woreda_nav_link_active': 'active',
		'district_woreda_add_form':district_woreda_add_form,
	}
    return render(request, 'district_woredas/district_woreda_add.html', context)

def district_woreda_detail_view(request, id=id):
	obj = get_object_or_404(District_Woreda, id=id)
	context = {
		'title': 'District/Woreda Detail',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'district_woreda_nav_link_active': 'active',
		'obj':obj,
	}
	return render(request, 'district_woredas/district_woreda_detail.html', context)

def district_woreda_update_view(request, id=id):
	obj = get_object_or_404(District_Woreda, id=id)
	district_woreda_update_form = AddDistrictWoredaForm(request.POST or None, instance=obj)
	if district_woreda_update_form.is_valid():
		district_woreda_update_form.save()
		messages.success(request, "District/Woreda has been Updated successfully")
		return redirect('district_woreda_list')
	context = {
		'title': 'District/Woreda Update',
		'school_open_menu': 'menu-open',
		'school_open_menu_active': 'active',
		'district_woreda_nav_link_active': 'active',
		'district_woreda_update_form':district_woreda_update_form,
	}
	return render(request, 'district_woredas/district_woreda_update.html', context)

def district_woreda_delete_view(request, id=id):
	obj = get_object_or_404(District_Woreda, id=id)
	obj.delete()
	messages.success(request, "District/Woreda has been Deleted successfully")
	return redirect('district_woreda_list')
###################### End Views for managing District/Woreda ######################