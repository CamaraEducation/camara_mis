from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Computer

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    user = request.user.userprofile.hub
    processed = Computer.objects.filter(working_status='Processed').filter(hub=user).count()
    working = Computer.objects.filter(working_status='working').filter(hub=user).count()
    problematic = Computer.objects.filter(working_status='Problematic').filter(hub=user).count()
    ewaste = Computer.objects.filter(working_status='E-Waste').filter(hub=user).count()
    dispatched = Computer.objects.filter(working_status='Dispatched').filter(hub=user).count()
    data = Computer.objects.all().filter(hub=user)
    corei3= Computer.objects.filter(processor_type='intel i3').filter(hub=user).count()
    corei5= Computer.objects.filter(processor_type='intel i5').filter(hub=user).count()
    corei7= Computer.objects.filter(processor_type='intel i7').filter(hub=user).count()
    dual_core= Computer.objects.filter(processor_type='Dual Core').filter(hub=user).count()
    dell = Computer.objects.filter(brand='Dell').filter(hub=user).count()
    hp = Computer.objects.filter(brand='HP').filter(hub=user).count()
    lenovo = Computer.objects.filter(brand='Lenovo').filter(hub=user).count()
    five12 = Computer.objects.filter(memory_size='512 MB').filter(hub=user).count()
    one_gb = Computer.objects.filter(memory_size='1 GB').filter(hub=user).count()
    two_gb = Computer.objects.filter(memory_size='2 GB').filter(hub=user).count()
    four_gb = Computer.objects.filter(memory_size='4 GB').filter(hub=user).count()
    egiht_gb = Computer.objects.filter(memory_size='8 GB').filter(hub=user).count()
    context = {
        'data':data,
        'corei3':corei3,
        'corei5':corei5,
        'corei7':corei7,
        'dual_core':dual_core,
        'dell':dell,
        'hp':hp,
        'lenovo':lenovo,
        'five12':five12,
        'one_gb':one_gb,
        'two_gb':two_gb,
        'four_gb':four_gb,
        'egiht_gb':egiht_gb,
        'processed':processed,
        'working':working,
        'problematic':problematic,
        'ewaste':ewaste,
        'dispatched':dispatched,
        'dashboard_open_menu': 'menu-open',
	    'dashboard_open_menu_active': 'active',
	    'computer_dashboard_nav_link_active': 'active',
    }
    return render(request, 'dashboards/dashboard.html',context)
