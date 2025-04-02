from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers

from .models import Customer


# Create your views here.

def viewCustomer(request):
    render_dict = {}
    customerList = Customer.objects.all().order_by('name')
    render_dict['customerList'] = customerList
    return render(request, 'customer.html', render_dict)


def insertCustomer(request):
    json_data = {}
    name = request.POST['name']
    address = request.POST['address']
    number = request.POST['number']

    varify = Customer.objects.filter(name=name, number=number).exists()
    if varify == False:
        add = Customer(name=name, address=address, number=number)
        add.save()
        json_data['exist'] = 'no'
    else:
        json_data['exist'] = 'yes'

    get = Customer.objects.get(name=name, number=number)
    json_data['id'] = get.id
    json_data['name'] = name
    json_data['address'] = address
    json_data['number'] = number

    return JsonResponse(json_data)


def deleteCustomer(request):
    json_data = {}
    customerId = request.GET['customerId']
    Customer.objects.get(pk=customerId).delete()
    json_data['customerId'] = customerId
    return JsonResponse(json_data)


def editCustomer(request):
    customerId = request.GET['customerId']
    json_data = serializers.serialize("json", [Customer.objects.get(pk=customerId)])
    return JsonResponse(json_data, safe=False)


def updateCustomer(request):
    customerId = request.POST['customerId']
    name = request.POST['name']
    address = request.POST['address']
    number = request.POST['number']
    update = Customer.objects.get(pk=customerId)
    update.name = name
    update.address = address
    update.number = number
    update.save()
    json_data = serializers.serialize("json", [update])
    return JsonResponse(json_data, safe=False)
