import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import Hub
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
	obj = get_object_or_404(School, id=id)
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
    county_region_add_form = AddCountyRegionForm(request.POST or None)
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