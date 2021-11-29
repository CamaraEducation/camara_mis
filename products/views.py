import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.models import Hub
from .models import Monitor, Supplier, Computer
from .forms import AddSuplierForm, AddComputerForm, AddMonitorForm, UploadComputerForm, UploadMonitorForm
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
    processed = Computer.objects.filter(working_status='Processed')
    working = Computer.objects.filter(working_status='working')
    problematic = Computer.objects.filter(working_status='Problematic')
    ewaste = Computer.objects.filter(working_status='E-Waste')
    dispatched = Computer.objects.filter(working_status='Dispatched')
    context = {
		'title': 'Computer List',
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'computers_list': computers_list,
		'processed': processed,
		'working': working,
		'problematic': problematic,
		'ewaste': ewaste,
		'dispatched':dispatched,
	}
    return render(request, 'computers/computer_list.html', context)

def computer_add_view(request):
    computer_add_form = AddComputerForm(request.POST or None)
    hubs = Hub.objects.all()
    if computer_add_form.is_valid():
        get_hub = request.POST.get("hub")
        hub = get_object_or_404(Hub, id=get_hub)
        computer_add_form.hub = hub
        computer_add_form.save()
        messages.success(request, "Computer added successfully")
        return redirect('computer_list')
    context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'title':'Add A Computer',
		'computer_add_form':computer_add_form,
		'hubs':hubs,
	}
    return render(request, 'computers/computer_add.html', context)

def computer_detail_view(request, id=id):
	obj = get_object_or_404(Computer, id=id)
	context = {UploadComputerForm: 'active',
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


def computer_upload_view(request):
	computer_upload_form = UploadComputerForm()
	hubs = Hub.objects.all()
	if request.method == 'POST':
		try:
			csv_file = request.FILES['computer_upload']
			get_hub = request.POST.get("hub")
			hub = get_object_or_404(Hub, id=get_hub)
			if not csv_file.name.endswith('.csv'):
				messages.error(request, 'This is not a CSV file')

			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			next(io_string)
			for column in csv.reader(io_string, delimiter=',', quotechar='|'):
				_, created = Computer.objects.update_or_create(
					hub=hub,
					c_affritrack_number=column[0],
					serial_number=column[1],
					brand=column[2],
					model=column[3],
					container_number=column[4],
					device_status=column[5],
					processor_type=column[6],
					processor_speed=column[7],
					memory_type=column[8],
					memory_size=column[9],
					storage_type=column[10],
					storage_size=column[11],
					date_received=column[12],
					)

			messages.success(request,f'The Computers has been uploaded successfully!')
			return redirect('computer_list')
		# except:
		# 	messages.error(request, 'Please Check your file it looks like you have duplicated items in you file or with the database')
		except Exception as e:
			print (e)
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'computer_nav_link_active': 'active',
		'title':'Computer Upload',
		'computer_upload_form':computer_upload_form,
		'hubs':hubs,
	}
	return render(request, 'computers/computer_upload.html', context)


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
    hubs = Hub.objects.all()
    if monitor_add_form.is_valid():
        get_hub = request.POST.get("hub")
        hub = get_object_or_404(Hub, id=get_hub)
        monitor_add_form.hub = hub
        monitor_add_form.save()
        messages.success(request, "Monitor added successfully")
        return redirect('monitor_list')
    context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'title':'Add A Monitor',
		'monitor_add_form':monitor_add_form,
		'hubs':hubs,
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

def monitor_upload_view(request):
	monitor_upload_form = UploadMonitorForm()
	hubs = Hub.objects.all()
	if request.method == 'POST':
		try:
			csv_file = request.FILES['monitor_upload']
			get_hub = request.POST.get("hub")
			hub = get_object_or_404(Hub, id=get_hub)
			if not csv_file.name.endswith('.csv'):
				messages.error(request, 'This is not a CSV file')

			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			next(io_string)
			for column in csv.reader(io_string, delimiter=',', quotechar='|'):
				_, created = Monitor.objects.update_or_create(
					hub=hub,
					m_affritrack_number=column[0],
					serial_number=column[1],
					brand=column[2],
					container_number=column[3],
					device_status=column[4],
					screen_size=column[5],
					date_received=column[6],
					)

			messages.success(request,f'The monitors has been uploaded successfully!')
			return redirect('monitor_list')
		# except:
		# 	messages.error(request, 'Please Check your file it looks like you have duplicated items in you file or with the database')
		except Exception as e:
			print (e)
	context = {
		'product_open_menu': 'menu-open',
		'product_open_menu_active': 'active',
		'monitor_nav_link_active': 'active',
		'title':'Monitor Upload',
		'monitor_upload_form':monitor_upload_form,
		'hubs':hubs,
	}
	return render(request, 'monitors/monitor_upload.html', context)
###################### End Views for managing Monitor ######################