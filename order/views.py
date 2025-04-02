from django.shortcuts import render
from measurement.models import Measurement, Order


def viewOrder(request):
    render_dict = {}
    orderList = Order.objects.all()
    render_dict['pending_OrderList'] = orderList.filter(status='pending')
    render_dict['done_OrderList'] = orderList.filter(status='done')
    return render(request, 'order.html', render_dict)


def insertOrder(request):
    pass


def deleteOrder(request):
    pass


def editOrder(request):
    pass


def updateOrder(request):
    pass
