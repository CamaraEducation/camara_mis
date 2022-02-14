from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Project, Donor, Partner, Project_Donor, Project_Partner
from .forms import AddProjectForm, AddDonorForm, AddPartnerForm, AddProjectPartnerForm, AddProjectDonorForm

###################### Views for managing Project ######################
def project_list_view(request):
	user = request.user.userprofile.hub
	project_list = Project.objects.all().filter(hub=user)
	context = {
		'title': 'Projects List',
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_nav_link_active': 'active',
		'project_list': project_list
	}
	return render(request, 'projects/project_list.html', context)

def project_add_view(request):
	project_add_form = AddProjectForm(request.POST or None)
	if project_add_form.is_valid():
		project_add_form.save()
		messages.success(request, "Project added successfully")
		return redirect('project_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_nav_link_active': 'active',
		'title':'Add A Project',
		'project_add_form':project_add_form,
	}
	return render(request, 'projects/project_add.html', context)

def project_detail_view(request, id=id):
	obj = get_object_or_404(Project, id=id)
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_nav_link_active': 'active',
		'title':'Project Detial',
		'obj':obj,
	}
	return render(request, 'projects/project_detail.html', context)

def project_update_view(request, id=id):
	obj = get_object_or_404(Project, id=id)
	project_update_form = AddProjectForm(request.POST or None, instance=obj)
	if project_update_form.is_valid():
		project_update_form.save()
		messages.success(request, "Project Updated successfully")
		return redirect('project_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_nav_link_active': 'active',
		'title':'Update Project',
		'project_update_form':project_update_form,
	}
	return render(request, 'projects/project_update.html', context)

def project_delete_view(request, id=id):
	obj = get_object_or_404(Project, id=id)
	obj.delete()
	messages.success(request, "Project Deleted successfully")
	return redirect('project_list')

###################### End Views for managing Project ######################

###################### Views for managing Donor ######################
def donor_list_view(request):
	donor_list = Donor.objects.all()
	context = {
		'title': 'Donors List',
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'donor_nav_link_active': 'active',
		'donor_list': donor_list
	}
	return render(request, 'donors/donor_list.html', context)

def donor_add_view(request):
	donor_add_form = AddDonorForm(request.POST or None)
	if donor_add_form.is_valid():
		donor_add_form.save()
		messages.success(request, "Donor added successfully")
		return redirect('donor_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'donor_nav_link_active': 'active',
		'title':'Add A Donor',
		'donor_add_form':donor_add_form,
	}
	return render(request, 'donors/donor_add.html', context)

def donor_detail_view(request, id=id):
	obj = get_object_or_404(Donor, id=id)
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'donor_nav_link_active': 'active',
		'title':'Donor Detial',
		'obj':obj,
	}
	return render(request, 'donors/donor_detail.html', context)

def donor_update_view(request, id=id):
	obj = get_object_or_404(Donor, id=id)
	donor_update_form = AddDonorForm(request.POST or None, instance=obj)
	if donor_update_form.is_valid():
		donor_update_form.save()
		messages.success(request, "Donor Updated successfully")
		return redirect('donor_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'donor_nav_link_active': 'active',
		'title':'Update Donor',
		'donor_update_form':donor_update_form,
	}
	return render(request, 'donors/donor_update.html', context)

def donor_delete_view(request, id=id):
	obj = get_object_or_404(Donor, id=id)
	obj.delete()
	messages.success(request, "Donor Deleted successfully")
	return redirect('donor_list')

###################### End Views for managing Donor ######################

###################### Views for managing Partners ######################
def partner_list_view(request):
	partner_list = Partner.objects.all()
	context = {
		'title': 'Partners List',
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'partner_nav_link_active': 'active',
		'partner_list': partner_list
	}
	return render(request, 'partners/partner_list.html', context)

def partner_add_view(request):
	partner_add_form = AddPartnerForm(request.POST or None)
	if partner_add_form.is_valid():
		partner_add_form.save()
		messages.success(request, "Partner added successfully")
		return redirect('partner_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'partner_nav_link_active': 'active',
		'title':'Add A Partner',
		'partner_add_form':partner_add_form,
	}
	return render(request, 'partners/partner_add.html', context)

def partner_detail_view(request, id=id):
	obj = get_object_or_404(Partner, id=id)
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'partner_nav_link_active': 'active',
		'title':'Partner Detial',
		'obj':obj,
	}
	return render(request, 'partners/partner_detail.html', context)

def partner_update_view(request, id=id):
	obj = get_object_or_404(Partner, id=id)
	partner_update_form = AddPartnerForm(request.POST or None, instance=obj)
	if partner_update_form.is_valid():
		partner_update_form.save()
		messages.success(request, "Partner Updated successfully")
		return redirect('partner_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'partner_nav_link_active': 'active',
		'title':'Update Partner',
		'partner_update_form':partner_update_form,
	}
	return render(request, 'partners/partner_update.html', context)

def partner_delete_view(request, id=id):
	obj = get_object_or_404(Partner, id=id)
	obj.delete()
	messages.success(request, "Partner Deleted successfully")
	return redirect('partner_list')

###################### End Views for managing Partner ######################


###################### Views for managing Project Partners ######################
def project_partner_list_view(request):
	project_partner_list = Project_Partner.objects.all()
	context = {
		'title': 'Project Partners List',
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_partner_nav_link_active': 'active',
		'project_partner_list': project_partner_list
	}
	return render(request, 'project_partners/project_partner_list.html', context)

def project_partner_add_view(request):
	project_partner_add_form = AddProjectPartnerForm(request.POST or None)
	if project_partner_add_form.is_valid():
		project_partner_add_form.save()
		messages.success(request, "Project Partner added successfully")
		return redirect('project_partner_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_partner_nav_link_active': 'active',
		'title':'Add A Project Partner',
		'project_partner_add_form':project_partner_add_form,
	}
	return render(request, 'project_partners/project_partner_add.html', context)

def project_partner_detail_view(request, id=id):
	obj = get_object_or_404(Project_Partner, id=id)
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_partner_nav_link_active': 'active',
		'title':'Project Partner Detial',
		'obj':obj,
	}
	return render(request, 'project_partners/project_partner_detail.html', context)

def project_partner_update_view(request, id=id):
	obj = get_object_or_404(Project_Partner, id=id)
	project_partner_update_form = AddProjectPartnerForm(request.POST or None, instance=obj)
	if project_partner_update_form.is_valid():
		project_partner_update_form.save()
		messages.success(request, "Project Partner Updated successfully")
		return redirect('project_partner_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_partner_nav_link_active': 'active',
		'title':'Update Project Partner',
		'project_partner_update_form':project_partner_update_form,
	}
	return render(request, 'project_partners/project_partner_update.html', context)

def project_partner_delete_view(request, id=id):
	obj = get_object_or_404(Project_Partner, id=id)
	obj.delete()
	messages.success(request, "Project Partner Deleted successfully")
	return redirect('project_partner_list')

###################### End Views for managing Project Partner ######################

###################### Views for managing Project Donor ######################
def project_donor_list_view(request):
	project_donor_list = Project_Donor.objects.all()
	context = {
		'title': 'Project Donors List',
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_donor_nav_link_active': 'active',
		'project_donor_list': project_donor_list
	}
	return render(request, 'project_donors/project_donor_list.html', context)

def project_donor_add_view(request):
	project_donor_add_form = AddProjectDonorForm(request.POST or None)
	if project_donor_add_form.is_valid():
		project_donor_add_form.save()
		messages.success(request, "Project Donor added successfully")
		return redirect('project_donor_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_donor_nav_link_active': 'active',
		'title':'Add A Project Donor',
		'project_donor_add_form':project_donor_add_form,
	}
	return render(request, 'project_donors/project_donor_add.html', context)

def project_donor_detail_view(request, id=id):
	obj = get_object_or_404(Project_Donor, id=id)
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_donor_nav_link_active': 'active',
		'title':'Project Donor Detial',
		'obj':obj,
	}
	return render(request, 'project_donors/project_donor_detail.html', context)

def project_donor_update_view(request, id=id):
	obj = get_object_or_404(Project_Donor, id=id)
	project_donor_update_form = AddProjectDonorForm(request.POST or None, instance=obj)
	if project_donor_update_form.is_valid():
		project_donor_update_form.save()
		messages.success(request, "Project Donor Updated successfully")
		return redirect('project_donor_list')
	context = {
		'project_open_menu': 'menu-open',
		'project_open_menu_active': 'active',
		'project_donor_nav_link_active': 'active',
		'title':'Update Project Donor',
		'project_donor_update_form':project_donor_update_form,
	}
	return render(request, 'project_donors/project_donor_update.html', context)

def project_donor_delete_view(request, id=id):
	obj = get_object_or_404(Project_Donor, id=id)
	obj.delete()
	messages.success(request, "Project Donor Deleted successfully")
	return redirect('project_donor_list')

###################### End Views for managing Project donor ######################