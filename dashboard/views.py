from django.shortcuts import render

from products.models import Computer

# Create your views here.
def home_view(request):
    processed = Computer.objects.filter(working_status='Processed').count()
    working = Computer.objects.filter(working_status='working').count()
    problematic = Computer.objects.filter(working_status='Problematic').count()
    ewaste = Computer.objects.filter(working_status='E-Waste').count()
    dispatched = Computer.objects.filter(working_status='Dispatched').count()
    data = Computer.objects.all()
    corei3= Computer.objects.filter(processor_type='intel i3').count()
    corei5= Computer.objects.filter(processor_type='intel i5').count()
    corei7= Computer.objects.filter(processor_type='intel i7').count()
    dual_core= Computer.objects.filter(processor_type='Dual Core').count()
    dell = Computer.objects.filter(brand='Dell').count()
    hp = Computer.objects.filter(brand='HP').count()
    lenovo = Computer.objects.filter(brand='Lenovo').count()
    five12 = Computer.objects.filter(memory_size='512MB').count()
    one_gb = Computer.objects.filter(memory_size='1GB').count()
    two_gb = Computer.objects.filter(memory_size='2GB').count()
    four_gb = Computer.objects.filter(memory_size='4GB').count()
    egiht_gb = Computer.objects.filter(memory_size='8GB').count()
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
