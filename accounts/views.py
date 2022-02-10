from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from .models import Department, Hub, Position, UserProfile
from .forms import AddOrganizationHubForm, AddDepartmentForm, AddPositionForm, AddUserProfileForm, AddUserForm, UpdateUserForm



##################### views for managing Users and Logins #####################
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('home')
            messages.error(request, "Your error message")
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_view.html', {'form': form, 'title': 'Login'})

def user_list_view(request):
	users_list = User.objects.all()
	context = {
		'title': 'Users List',
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'user_nav_link_active': 'active',
		'users_list': users_list
	}
	return render(request, 'accounts/user_list.html', context)

def user_add_view(request):
	if request.method == 'POST':
		user_add_form = AddUserForm(request.POST)
		user_profile_add_form = AddUserProfileForm(request.POST)
		if user_add_form.is_valid() and user_profile_add_form.is_valid():
			user = user_add_form.save()
			profile = user_profile_add_form.save(commit=False)
			profile.user = user
			profile.save()
			messages.success(request, "User added successfully")
			return redirect('user_list')
	else:
		user_add_form = AddUserForm()
		user_profile_add_form = AddUserProfileForm()

	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'user_nav_link_active': 'active',
		'title': 'Register',
		'user_add_form': user_add_form,
		'user_profile_add_form': user_profile_add_form
	}
	return render(request, 'accounts/user_add.html', context)

def user_detail_view(request, id=id):
	obj = get_object_or_404(User, id=id)
	obj2 = get_object_or_404(UserProfile, user=id)
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'user_nav_link_active': 'active',
		'title':'USer Detial',
		'obj':obj,
		'obj2':obj2,
	}
	return render(request, 'accounts/user_detail.html', context)

def user_update_view(request, id=id):
	obj = get_object_or_404(User, id=id)
	obj2 = get_object_or_404(UserProfile, id=id)
	user_update_form = UpdateUserForm(request.POST or None, instance=obj)
	user_profile_update_form = AddUserProfileForm(request.POST or None, instance=obj2)
	if user_update_form.is_valid():
		user_update_form.save()
		messages.success(request, "User Information Updated successfully")
		return redirect('user_list')

	elif user_profile_update_form.is_valid():
		user_profile_update_form.save()
		messages.success(request, "User Profile Information Updated successfully")
		return redirect('user_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'user_nav_link_active': 'active',
		'title':'Update user account and profile',
		'obj':obj,
		'user_update_form':user_update_form,
		'user_profile_update_form': user_profile_update_form
	}
	return render(request, 'accounts/user_update.html', context)

def user_deactivate_view(request, id=id):
	user = User.objects.get(pk=id)
	user.is_active = False
	user.save()
	messages.success(request, "User account has been successfully deactivated!")
	return redirect('user_list')

def user_activate_view(request, id=id):
	user = User.objects.get(pk=id)
	user.is_active = True
	user.save()
	messages.success(request, "User account has been successfully activated!")
	return redirect('user_list')

##################### End of views for managing Users and Logins #####################

##################### views for managing Hubs #####################
def organization_hub_list_view(request):
	organization_hub_list = Hub.objects.all()
	context = {
		'title': 'Hubs List',
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'hub_nav_link_active': 'active',
		'organization_hub_list': organization_hub_list
	}
	return render(request, 'hubs/hub_list.html', context)


def organization_hub_add_view(request):
	organization_hub_add_form = AddOrganizationHubForm(request.POST or None)
	if organization_hub_add_form.is_valid():
		organization_hub_add_form.save()
		messages.success(request, "Hub added successfully")
		return redirect('organization_hub_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'hub_nav_link_active': 'active',
		'title':'Add Hub',
		'organization_hub_add_form':organization_hub_add_form,
	}
	return render(request, 'hubs/hub_add.html', context)

def organization_hub_detail_view(request, id=id):
	obj = get_object_or_404(Hub, id=id)
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'hub_nav_link_active': 'active',
		'title':'Hub Detial',
		'obj':obj,
	}
	return render(request, 'hubs/hub_detail.html', context)

def organization_hub_update_view(request, id=id):
	obj = get_object_or_404(Hub, id=id)
	organization_hub_update_form = AddOrganizationHubForm(request.POST or None, instance=obj)
	if organization_hub_update_form.is_valid():
		organization_hub_update_form.save()
		messages.success(request, "Hub Updated successfully")
		return redirect('organization_hub_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'hub_nav_link_active': 'active',
		'title':'Update Hub',
		'organization_hub_update_form':organization_hub_update_form,
	}
	return render(request, 'hubs/hub_update.html', context)

def organization_hub_delete_view(request, id=id):
	obj = get_object_or_404(Hub, id=id)
	obj.delete()
	messages.success(request, "Hub Deleted successfully")
	return redirect('organization_hub_list')
##################### End of views for managing Hubs #####################

##################### views for managing Department #####################
def department_list_view(request):
	department_list = Department.objects.all()
	context = {
		'title': 'Departments List',
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'department_nav_link_active': 'active',
		'department_list': department_list
	}
	return render(request, 'departments/department_list.html', context)

def department_add_view(request):
	department_add_form = AddDepartmentForm(request.POST or None)
	if department_add_form.is_valid():
		department_add_form.save()
		messages.success(request, "Department added successfully")
		return redirect('department_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'department_nav_link_active': 'active',
		'title':'Add Department',
		'department_add_form':department_add_form,
	}
	return render(request, 'departments/department_add.html', context)

def department_detail_view(request, id=id):
	obj = get_object_or_404(Department, id=id)
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'department_nav_link_active': 'active',
		'title':'Department Detial',
		'obj':obj,
	}
	return render(request, 'departments/department_detail.html', context)

def department_update_view(request, id=id):
	obj = get_object_or_404(Department, id=id)
	department_update_form = AddDepartmentForm(request.POST or None, instance=obj)
	if department_update_form.is_valid():
		department_update_form.save()
		messages.success(request, "Department Updated successfully")
		return redirect('department_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'department_nav_link_active': 'active',
		'title':'Update Department',
		'department_update_form':department_update_form,
	}
	return render(request, 'departments/department_update.html', context)

def department_delete_view(request, id=id):
	obj = get_object_or_404(Department, id=id)
	obj.delete()
	messages.success(request, "Department Deleted successfully")
	return redirect('department_list')
##################### end of views for managing Department #####################

##################### views for managing Job Positions #####################
def position_list_view(request):
	position_list = Position.objects.all()
	context = {
		'title': 'Job Position List',
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'position_nav_link_active': 'active',
		'position_list': position_list
	}
	return render(request, 'positions/position_list.html', context)

def position_add_view(request):
	position_add_form = AddPositionForm(request.POST or None)
	if position_add_form.is_valid():
		position_add_form.save()
		messages.success(request, "Position added successfully")
		return redirect('position_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'position_nav_link_active': 'active',
		'title':'Add Job Position',
		'position_add_form':position_add_form,
	}
	return render(request, 'positions/position_add.html', context)

def position_detail_view(request, id=id):
	obj = get_object_or_404(Position, id=id)
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'position_nav_link_active': 'active',
		'title':'Position Detial',
		'obj':obj,
	}
	return render(request, 'positions/position_detail.html', context)

def position_update_view(request, id=id):
	obj = get_object_or_404(Position, id=id)
	position_update_form = AddPositionForm(request.POST or None, instance=obj)
	if position_update_form.is_valid():
		position_update_form.save()
		messages.success(request, "Position Updated successfully")
		return redirect('position_list')
	context = {
		'account_open_menu': 'menu-open',
		'account_open_menu_active': 'active',
		'position_nav_link_active': 'active',
		'title':'Update Position',
		'position_update_form':position_update_form,
	}
	return render(request, 'positions/position_update.html', context)

def position_delete_view(request, id=id):
	obj = get_object_or_404(Position, id=id)
	obj.delete()
	messages.success(request, "Position Deleted successfully")
	return redirect('position_list')
##################### views for managing Job Positions #####################

##################### Ajax views for Hub, Department, and Position Dependent Dropdown #####################
def ajax_load_hub_department(request):
	if request.GET.get('hub_id'):
		hub_id = request.GET.get('hub_id')
		departments = Department.objects.filter(hub_id=hub_id)
		return render(request, 'positions/department_dropdown_option.html', {'departments': departments})
	else:
		department_id = request.GET.get('department_id')
		positions = Position.objects.filter(department_id=department_id)
		return render(request, 'positions/department_dropdown_option.html', {'positions': positions})
##################### End of Ajax views for Hub, Department, and Position Dependent Dropdown #####################