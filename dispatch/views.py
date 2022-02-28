from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from datetime import date
from dateutil.relativedelta import relativedelta
from .forms import AddComputerApplicantForm,AddComputerRequestForm, DispatchComputerForm
from dispatch.models import Computer_Applicant, Computer_Request, Dispatch
from school.models import School
from accounts.models import Hub, UserProfile
from products.models import Computer, Monitor

###################### Views for managing Computer Applicant ######################
def applicant_list_view(request):
    user = request.user.userprofile.hub
    computer_applicants_list = Computer_Applicant.objects.all().filter(hub=user)
    context = {
		'title': 'Computer Applicant List',
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'applicant_nav_link_active': 'active',
		'computer_applicants_list': computer_applicants_list
	}
    return render(request, 'applicants/applicant_list.html', context)

def applicant_add_view(request):
    applicant_add_form = AddComputerApplicantForm(request.POST or None)
    if applicant_add_form.is_valid():
        applicant_add_form.save()
        messages.success(request, "Computer Applicant added successfully")
        return redirect('dispatch:applicant_list')
    context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'applicant_nav_link_active': 'active',
		'title':'Add a computer applicant',
		'applicant_add_form':applicant_add_form,
	}
    return render(request, 'applicants/applicant_add.html', context)

def applicant_detail_view(request, id=id):
	obj = get_object_or_404(Computer_Applicant, id=id)
	context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'applicant_nav_link_active': 'active',
		'title':'Computer Applicant Detial',
		'obj':obj,
	}
	return render(request, 'applicants/applicant_detail.html', context)

def applicant_update_view(request, id=id):
	obj = get_object_or_404(Computer_Applicant, id=id)
	applicant_update_form = AddComputerApplicantForm(request.POST or None, instance=obj)
	if applicant_update_form.is_valid():
		applicant_update_form.save()
		messages.success(request, "Computer Applicant Updated successfully")
		return redirect('dispatch:applicant_list')
	context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'applicant_nav_link_active': 'active',
		'title':'Update computer applicant',
		'applicant_update_form':applicant_update_form,
	}
	return render(request, 'applicants/applicant_update.html', context)

def applicant_delete_view(request, id=id):
	obj = get_object_or_404(Computer_Applicant, id=id)
	obj.delete()
	messages.success(request, "computer Applicant Deleted successfully")
	return redirect('dispatch:applicant_list')


###################### End Views for managing Computer Applicant ######################


###################### Views for managing Computer Request ######################

# The function below can add the number of computers a school is requesting
def school_computer_request_add(request, id=id):
	obj = get_object_or_404(School, id=id)
	computer_app = Computer_Applicant.objects.all()
	context = {
		'title':'Add Computer Request',
		'title': 'Computer Applicant List',
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_request_nav_link_active': 'active',
		'obj':obj,
		'computer_app':computer_app
	}
	return render(request, 'computer_requests/school_computer_request_add.html', context)


def computer_request_list_view(request):
    user = request.user.userprofile.hub
    computer_request_list = Computer_Request.objects.filter(request_status=0).filter(hub=user)
    context = {
		'title': 'Computer Applicant List',
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_request_nav_link_active': 'active',
		'computer_request_list': computer_request_list
	}
    return render(request, 'computer_requests/computer_request_list.html', context)

def computer_request_add_view(request):
	if request.method == 'POST':
		number_of_computers = request.POST.get('number_of_computers')
		school_name_form = request.POST.get('school_name')
		hub_from = request.POST.get('hub')
		applicant_from = request.POST.get('applicant_id')

		school_name = get_object_or_404(School, id=school_name_form)
		hub = get_object_or_404(Hub, id=hub_from)
		applicant_id = get_object_or_404(Computer_Applicant, id=applicant_from)

		obj = Computer_Request.objects.create(
			school_name=school_name,
			number_of_computers=number_of_computers,
			hub = hub,
			applicant_id=applicant_id)
		obj.save()
		return redirect('dispatch:computer_request_list')
	# context = {
	# 	'dispatch_open_menu': 'menu-open',
	# 	'dispatch_open_menu_active': 'active',
	# 	'computer_request_nav_link_active': 'active',
	# 	'title':'Add a computer Request',
	# }
	#return render(request, 'computer_requests/school_computer_request_add.html', context)

def computer_request_detail_view(request, id=id):
	obj = get_object_or_404(Computer_Request, id=id)
	context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_request_nav_link_active': 'active',
		'title':'Computer Applicant Detial',
		'obj':obj,
	}
	return render(request, 'computer_requests/school_computer_request_detail.html', context)

def computer_request_update_view(request, id=id):
	obj = get_object_or_404(Computer_Request, id=id)
	applicant_update_form = AddComputerApplicantForm(request.POST or None, instance=obj)
	if applicant_update_form.is_valid():
		applicant_update_form.save()
		messages.success(request, "Computer Applicant Updated successfully")
		return redirect('applicant_list')
	context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_request_nav_link_active': 'active',
		'title':'Update computer applicant',
		'applicant_update_form':applicant_update_form,
	}
	return render(request, 'computer_requests/computer_request_update.html', context)

def computer_request_delete_view(request, id=id):
	obj = get_object_or_404(Computer_Request, id=id)
	obj.delete()
	messages.success(request, "computer Applicant Deleted successfully")
	return redirect('applicant_list')

###################### Views for managing Computer Request ######################

def product_status_check(request):
	user = request.user.userprofile.hub
	if request.GET.get('paffritract_number', None):
		c_affritrack_number = request.GET.get('paffritract_number')
		check_status = Computer.objects.filter(c_affritrack_number=c_affritrack_number, working_status = 'Processed', hub=user)
		if check_status:
			response = {
					'is_taken': 5
				}
			return JsonResponse(response)
		else:
			response = {
					'is_taken': 1
				}
			return JsonResponse(response)
	if request.GET.get('maffritract_number', None):
		m_affritrack_number = request.GET.get('maffritract_number')
		check_status = Monitor.objects.filter(m_affritrack_number=m_affritrack_number, working_status = 'Processed', hub=user)
		if check_status:
			response = {
					'is_taken': 5
				}
			return JsonResponse(response)
		else:
			response = {
					'is_taken': 1
				}
			return JsonResponse(response)

def computer_request_dispatch_process_view(request, id=id):
	obj = get_object_or_404(Computer_Request, id=id)
	a = obj.number_of_computers + 1
	c = range(1, a, 1)
	
	context = {
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_request_nav_link_active': 'active',
        'title': 'Dispatch Computers',
        'obj': obj,
        'c': c,
    }
	return render(request, 'dispatchs/school_dispatch_add.html', context)


def computer_dispatch_view(request):
	if request.method == 'POST':
		# print(request.POST)
		counter = 1
		number_of_computers = int(request.POST.get('number_of_computers'))
		request_id = int(request.POST.get('request_id'))
		request_info = Computer_Request.objects.get(id=request_id)
		hub = request.POST.get('hub')
		hub_info = Hub.objects.get(id=hub)
		applicant_name = request.POST.get('applicant_id')
		applicant_info = Computer_Applicant.objects.get(id=applicant_name)
		school_name = request.POST.get('school_name')
		school_info = School.objects.get(id=school_name)
		date_dispatched = date.today()
		warranty_end = date_dispatched + relativedelta(years=1)
		dispatched_by = get_object_or_404(UserProfile, id=request.user.id)
		while counter <= number_of_computers:
			pc_affritrac = request.POST.get('affritract_number_'+ str(counter)) 
			mo_affritrac = request.POST.get('maffritract_number_'+ str(counter)) 
			obj = Dispatch.objects.create(
				hub = hub_info,
				computer_request_id = request_info,
				applicant_name=applicant_info,
				school_name=school_info,
				c_affritrack_number = pc_affritrac,
				m_affritrack_number = mo_affritrac,
				date_dispatched = date_dispatched,
				dispatched_by = dispatched_by,
				warranty_end = warranty_end,
				)
			obj.save()
			Computer.objects.filter(c_affritrack_number=pc_affritrac).update(working_status='Dispatched')
			Monitor.objects.filter(m_affritrack_number=mo_affritrac).update(working_status='Dispatched')
			counter += 1

			Computer_Request.objects.filter(id=request_id).update(request_status=1)
		return redirect('dispatch:computer_request_list')

def computer_dispatch_list_view(request):
    user = request.user.userprofile.hub
    computer_dispatch_list = Computer_Request.objects.filter(request_status=1).filter(hub=user)
    context = {
		'title': 'Computer Dispatched List',
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_dispath_nav_link_active': 'active',
		'computer_dispatch_list': computer_dispatch_list
	}
    return render(request, 'computer_dispatch/computer_dispatch_list.html', context)		

def computer_dispatch_print_view(request, id=id):
	obj = Dispatch.objects.filter(computer_request_id=id)
	dis_data = get_object_or_404(Computer_Request, id=id)
	context = {
		'title': 'Computer Dispatched List',
		'dispatch_open_menu': 'menu-open',
		'dispatch_open_menu_active': 'active',
		'computer_dispath_nav_link_active': 'active',
		'obj': obj,
		'dis_data': dis_data
	}
	return render(request, 'computer_dispatch/computer_dispatch_detail.html', context)

# def computer_dispatch_view(request):
# 	computer_dispatch_form = DispatchComputerForm(request.POST or None)
# 	if computer_dispatch_form.is_valid():
# 		request_id = request.POST.get('request_id')
# 		number_of_computers = request.POST.get('number_of_computers')
# 		request_info = get_object_or_404(Computer_Request, id=request_id)
# 		hub = request_info['hub']
# 		computer_request_id = request_id
# 		applicant_name = request_info['applicant_id']
# 		school_name = request_info['school_name']

# 		for num_of_com in range(1, number_of_computers):
# 			computer_dispatch_form.hub = hub
# 			computer_dispatch_form.computer_request_id = computer_request_id
# 			computer_dispatch_form.applicant_name = applicant_name
# 			computer_dispatch_form.school_name = school_name
# 			computer_dispatch_form.c_affritrack_number = request.POST.get('affritract_number_') + num_of_com
# 			computer_dispatch_form.m_affritrack_number = request.POST.get('maffritract_number_') + num_of_com
# 			computer_dispatch_form.save()
		
# 		messages.success(request, "Computer Dispatched successfully")
# 		return redirect('computer_request_list')

# 	context = {
# 		'computer_dispatch_form': computer_dispatch_form
# 	}
# 	return render(request, 'dispatchs/school_dispatch_add.html', context)


