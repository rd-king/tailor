from django.shortcuts import render
from customer.models import Customer
from measurement.models import Measurement, Order


# Create your views here.

def viewDashbord(request):
    render_dict = {}
    render_dict['total_customer'] = len(Customer.objects.all())
    render_dict['total_order'] = len(Order.objects.all())

    render_dict['pending_order'] = Order.objects.filter(status='pending').order_by('-id')
    if len(render_dict['pending_order']) > 10:
        render_dict['pending_order'] = render_dict['pending_order'][10]

    print(">>>>>>>>>", render_dict)
    return render(request, 'index.html', render_dict)
