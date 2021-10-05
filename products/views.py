from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Monitor, Supplier, Computer
from .forms import AddSuplierForm, AddComputerForm, AddMonitorForm
# Create your views here.


###################### Views for managing Supplier ######################
def supplier_list_view(request):
    suppliers_list = Supplier.objects.all()
    context = {
		'title': 'Supplier List',
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'supplier_nav_link_active': 'active',
		'suppliers_list': suppliers_list
	}
    return render(request, 'suppliers/supplier_list.html', context)

def supplier_add_view(request):
    supplier_add_form = AddSuplierForm(request.POST or None)
    if supplier_add_form.is_valid():
        supplier_add_form.save()
        messages.success(request, "Supplier added successfully")
        return redirect('supplier_list')
    context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'supplier_nav_link_active': 'active',
		'title':'Add A Supplier',
		'supplier_add_form':supplier_add_form,
	}
    return render(request, 'suppliers/supplier_add.html', context)

def supplier_detail_view(request, id=id):
	obj = get_object_or_404(Supplier, id=id)
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'supplier_nav_link_active': 'active',
		'title':'Supplier Detial',
		'obj':obj,
	}
	return render(request, 'suppliers/supplier_detail.html', context)

def supplier_update_view(request, id=id):
	obj = get_object_or_404(Supplier, id=id)
	supplier_update_form = AddSuplierForm(request.POST or None, instance=obj)
	if supplier_update_form.is_valid():
		supplier_update_form.save()
		messages.success(request, "Supplier Updated successfully")
		return redirect('supplier_list')
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'supplier_nav_link_active': 'active',
		'title':'Update Supplier',
		'supplier_update_form':supplier_update_form,
	}
	return render(request, 'suppliers/supplier_update.html', context)

def supplier_delete_view(request, id=id):
	obj = get_object_or_404(Supplier, id=id)
	obj.delete()
	messages.success(request, "Supplier Deleted successfully")
	return redirect('supplier_list')

###################### End Views for managing Supplier ######################

###################### Views for managing Computer ######################
def computer_list_view(request):
    computers_list = Computer.objects.all()
    context = {
		'title': 'Computer List',
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'computers_list': computers_list
	}
    return render(request, 'computers/computer_list.html', context)

def computer_add_view(request):
    computer_add_form = AddComputerForm(request.POST or None)
    if computer_add_form.is_valid():
        computer_add_form.save()
        messages.success(request, "Computer added successfully")
        return redirect('computer_list')
    context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'title':'Add A Computer',
		'computer_add_form':computer_add_form,
	}
    return render(request, 'computers/computer_add.html', context)

def computer_detail_view(request, id=id):
	obj = get_object_or_404(Computer, id=id)
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'title':'Computer Detial',
		'obj':obj,
	}
	return render(request, 'computers/computer_detail.html', context)

def computer_update_view(request, id=id):
	obj = get_object_or_404(Computer, id=id)
	computer_update_form = AddComputerForm(request.POST or None, instance=obj)
	if computer_update_form.is_valid():
		computer_update_form.save()
		messages.success(request, "Computer Updated successfully")
		return redirect('computer_list')
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'title':'Update Computer',
		'computer_update_form':computer_update_form,
	}
	return render(request, 'computers/computer_update.html', context)

def computer_delete_view(request, id=id):
	obj = get_object_or_404(Computer, id=id)
	obj.delete()
	messages.success(request, "Computer Deleted successfully")
	return redirect('computer_list')

###################### End Views for managing Computer ######################

###################### Views for managing Monitor ######################
def monitor_list_view(request):
    monitors_list = Monitor.objects.all()
    context = {
		'title': 'Monitor List',
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'monitors_list': monitors_list
	}
    return render(request, 'monitors/monitor_list.html', context)

def monitor_add_view(request):
    monitor_add_form = AddMonitorForm(request.POST or None)
    if monitor_add_form.is_valid():
        monitor_add_form.save()
        messages.success(request, "Monitor added successfully")
        return redirect('monitor_list')
    context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'title':'Add A Monitor',
		'monitor_add_form':monitor_add_form,
	}
    return render(request, 'monitors/monitor_add.html', context)

def monitor_detail_view(request, id=id):
	obj = get_object_or_404(Monitor, id=id)
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'title':'Monitor Detial',
		'obj':obj,
	}
	return render(request, 'monitors/monitor_detail.html', context)

def monitor_update_view(request, id=id):
	obj = get_object_or_404(Monitor, id=id)
	monitor_update_form = AddMonitorForm(request.POST or None, instance=obj)
	if monitor_update_form.is_valid():
		monitor_update_form.save()
		messages.success(request, "Monitor Updated successfully")
		return redirect('monitor_list')
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'title':'Update Monitor',
		'monitor_update_form':monitor_update_form,
	}
	return render(request, 'monitors/monitor_update.html', context)

def monitor_delete_view(request, id=id):
	obj = get_object_or_404(Monitor, id=id)
	obj.delete()
	messages.success(request, "Monitor Deleted successfully")
	return redirect('monitor_list')

###################### End Views for managing Monitor ######################