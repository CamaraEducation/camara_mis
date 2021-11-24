from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AddComputerApplicantForm,AddComputerRequestForm
from dispatch.models import Computer_Applicant, Computer_Request
from school.models import School
from accounts.models import Hub
from products.models import Computer, Monitor

###################### Views for managing Computer Applicant ######################
def applicant_list_view(request):
    computer_applicants_list = Computer_Applicant.objects.all()
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

# def ajax_load_school(request):
# 	if request.GET.get('hub_id'):
# 		hub_id = request.GET.get('hub_id')
# 		school_names = School.objects.filter(country=hub_id)
# 		return render(request, 'applicants/applicant_dropdown_option.html', {'school_names': school_names})
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
    computer_request_list = Computer_Request.objects.all()
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

def computer_request_dispatch_process_view(request, id=id):
	obj = get_object_or_404(Computer_Request, id=id)
	a = obj.number_of_computers + 1
	c = range(1, a, 1)
	context = {
        'title': 'Dispatch Computers',
        'obj': obj,
        'c': c,
    }
	return render(request, 'dispatchs/school_dispatch_add.html', context)

def product_status_check(request):
	if request.GET.get('affritract_number'):
		c_affritrack_number = request.GET.get('affritract_number')
		if c_affritrack_number:
				pdata = Computer.objects.filter(c_affritrack_number=c_affritrack_number)
				if(pdata):
					return render(request, 'dispatch/school_dispatch_add.html',{'pdata': pdata})
    # else:
    #     affritract_number = request.GET.get('maffritract_number')
    #     if affritract_number:
    #         response = {
    #             'mdata': Monitor.objects.filter(affritract_number=affritract_number)
    #             }
    #         # mdata = Monitor.objects.filter(affritract_number=affritract_number, status=2)
    #         # messages.success(request,f'School Computer request has been Added successfully!')
    #         # return render(request, 'dispatch/school_dispatch_add.html',{'mdata': mdata})
    #         if (response):
    #             return render(request, 'dispatch/school_dispatch_add.html',{'response': response})