from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Computer
from django.db.models import Count
from django.db.models.functions import TruncDay

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    user = request.user.userprofile.hub
    data = Computer.objects.all().filter(hub=user)

    processed = Computer.objects.filter(working_status='Processed').filter(hub=user).count()
    working = Computer.objects.filter(working_status='working').filter(hub=user).count()
    problematic = Computer.objects.filter(working_status='Problematic').filter(hub=user).count()
    ewaste = Computer.objects.filter(working_status='E-Waste').filter(hub=user).count()
    dispatched = Computer.objects.filter(working_status='Dispatched').filter(hub=user).count()
    not_received = Computer.objects.filter(working_status='Not Received').filter(hub=user).count()

    processor_type = Computer.objects.filter(hub=user).values('processor_type').annotate(total=Count('id')).order_by('processor_type')
    computer_ram_size = Computer.objects.filter(hub=user).values('memory_size').annotate(total=Count('id')).order_by('memory_size')
    dailydata = Computer.objects.filter(working_status='Processed').filter(hub=user).annotate(date=TruncDay('date_modified'))\
        .values("date").annotate(updated_count=Count('id')).order_by("date")
    brands = Computer.objects.filter(hub=user).values('brand').annotate(total=Count('id')).order_by('brand')
    context = {
        'dailydata':dailydata,
        'processor_type':processor_type,
        'computer_ram_size':computer_ram_size,
        'data':data,
        'brands':brands,
        'processed':processed,
        'working':working,
        'problematic':problematic,
        'ewaste':ewaste,
        'dispatched':dispatched,
        'not_received':not_received,
        'dashboard_open_menu': 'menu-open',
	    'dashboard_open_menu_active': 'active',
	    'computer_dashboard_nav_link_active': 'active',
    }
    return render(request, 'dashboards/dashboard.html',context)
