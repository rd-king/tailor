from django.shortcuts import render
from .models import Measurement, Order
from django.core import serializers
from django.http import JsonResponse
import json
import os
from django.conf import settings
from customer.models import Customer


# Create your views here.
class MeasurementORM:
    def createMeasurement(self, measurement):
        create = Measurement(lambai_pent=measurement.lambai_pent,
                             kamar_pent=measurement.kamar_pent,
                             seet_pent=measurement.seet_pent,
                             mori_pent=measurement.mori_pent,
                             jangh_pent=measurement.jangh_pent,
                             jolo_pent=measurement.jolo_pent,
                             gothan_pent=measurement.gothan_pent,
                             lees_pent=measurement.lees_pent,
                             lambai_shirt=measurement.lambai_shirt,
                             chati_shirt=measurement.chati_shirt,
                             bay_shirt=measurement.bay_shirt,
                             solder_shirt=measurement.solder_shirt,
                             kamar_shirt=measurement.kamar_shirt,
                             pech_shirt=measurement.pech_shirt,
                             kolar_shirt=measurement.kolar_shirt,
                             kaf_shirt=measurement.kaf_shirt,
                             measurement_CustomerId_id=measurement.customerId)
        create.save()
        return create

    def viewFilterMeasurement(self, measurementId):
        view = Measurement.objects.filter(measurement_CustomerId=measurementId)
        return view

    def deleteMeasurement(self, measurementId):
        Measurement.objects.get(pk=measurementId).delete()

    def getMeasurement(self, measurementId):
        get = Measurement.objects.get(pk=measurementId)
        return get


def viewMeasurement(request):
    render_dict = {}
    customerId = request.GET['customerId']

    render_dict['getCustomer'] = Customer.objects.get(pk=customerId)

    measurementList = Measurement.objects.filter(measurement_CustomerId_id=customerId)
    orderList = Order.objects.filter(order_CustomerId_id=customerId)

    if len(measurementList) != 0:
        render_dict['measurementList'] = measurementList
    if len(orderList) != 0:
        render_dict['orderList'] = orderList.filter(status='pending').order_by('-id')
        render_dict['historyList'] = orderList.filter(status='done').order_by('-id')

    return render(request, 'measurement.html', render_dict)


def insertMeasurement(request):
    measurement = Measurement()
    measurementORM = MeasurementORM()

    measurement.lambai_pent = request.POST['lambai_pent']
    measurement.kamar_pent = request.POST['kamar_pent']
    measurement.seet_pent = request.POST['seet_pent']
    measurement.mori_pent = request.POST['mori_pent']
    measurement.jangh_pent = request.POST['jangh_pent']
    measurement.jolo_pent = request.POST['jolo_pent']
    measurement.gothan_pent = request.POST['gothan_pent']
    measurement.lees_pent = request.POST['lees_pent']

    measurement.lambai_shirt = request.POST['lambai_shirt']
    measurement.chati_shirt = request.POST['chati_shirt']
    measurement.bay_shirt = request.POST['bay_shirt']
    measurement.solder_shirt = request.POST['solder_shirt']
    measurement.kamar_shirt = request.POST['kamar_shirt']
    measurement.pech_shirt = request.POST['pech_shirt']
    measurement.kolar_shirt = request.POST['kolar_shirt']
    measurement.kaf_shirt = request.POST['kaf_shirt']
    measurement.customerId = request.POST['customerId']

    create = measurementORM.createMeasurement(measurement)

    json_data = serializers.serialize("json", [create])
    return JsonResponse(json_data, safe=False)


def deleteMeasurement(request):
    measurementORM = MeasurementORM()
    measurementId = request.GET['measurementId']
    deleteMeasurement = measurementORM.getMeasurement(measurementId)
    measurementORM.deleteMeasurement(measurementId)
    json_data = serializers.serialize("json", [deleteMeasurement])
    return JsonResponse(json_data, safe=False)


def editMeasurement(request):
    measurementId = request.GET['measurementId']
    edit = Measurement.objects.get(pk=measurementId)
    json_data = serializers.serialize("json", [edit])
    return JsonResponse(json_data, safe=False)


def updateMeasurement(request):
    print(">>>", request.POST)
    measurementId = request.POST['measurementId']
    update = Measurement.objects.get(pk=measurementId)

    update.lambai_pent = request.POST['lambai_pent']
    update.kamar_pent = request.POST['kamar_pent']
    update.seet_pent = request.POST['seet_pent']
    update.mori_pent = request.POST['mori_pent']
    update.jangh_pent = request.POST['jangh_pent']
    update.jolo_pent = request.POST['jolo_pent']
    update.gothan_pent = request.POST['gothan_pent']
    update.lees_pent = request.POST['lees_pent']

    update.lambai_shirt = request.POST['lambai_shirt']
    update.chati_shirt = request.POST['chati_shirt']
    update.bay_shirt = request.POST['bay_shirt']
    update.solder_shirt = request.POST['solder_shirt']
    update.kamar_shirt = request.POST['kamar_shirt']
    update.pech_shirt = request.POST['pech_shirt']
    update.kolar_shirt = request.POST['kolar_shirt']
    update.kaf_shirt = request.POST['kaf_shirt']
    update.customerId = request.POST['customerId']

    update.save()

    json_data = serializers.serialize("json", [update])
    return JsonResponse(json_data, safe=False)


def insertOrder(request):
    print(">>>", request.POST)

    customerId = request.POST['customerId']
    create = Order(order_CustomerId_id=customerId)

    create.lambai_pent = request.POST['lambai_pent']
    create.kamar_pent = request.POST['kamar_pent']
    create.seet_pent = request.POST['seet_pent']
    create.mori_pent = request.POST['mori_pent']
    create.jangh_pent = request.POST['jangh_pent']
    create.jolo_pent = request.POST['jolo_pent']
    create.gothan_pent = request.POST['gothan_pent']
    create.lees_pent = request.POST['lees_pent']
    create.vigat_pent = request.POST['vigat_pent']

    create.lambai_shirt = request.POST['lambai_shirt']
    create.chati_shirt = request.POST['chati_shirt']
    create.bay_shirt = request.POST['bay_shirt']
    create.solder_shirt = request.POST['solder_shirt']
    create.kamar_shirt = request.POST['kamar_shirt']
    create.pech_shirt = request.POST['pech_shirt']
    create.kolar_shirt = request.POST['kolar_shirt']
    create.kaf_shirt = request.POST['kaf_shirt']
    create.vigat_shirt = request.POST['vigat_shirt']

    if request.FILES.get('photo') != None:
        create.photo = request.FILES['photo']

    create.save()
    json_data = serializers.serialize("json", [create])
    return JsonResponse(json_data, safe=False)


def deleteOrder(request):
    orderId = request.GET['orderId']
    delete = Order.objects.get(pk=orderId)
    json_data = serializers.serialize("json", [delete])
    if delete.photo != '':
        path = delete.photo.path
        os.remove(str(path))
    delete.delete()
    return JsonResponse(json_data, safe=False)


def editOrder(request):
    orderId = request.GET['orderId']
    edit = Order.objects.get(pk=orderId)
    json_data = serializers.serialize("json", [edit])
    return JsonResponse(json_data, safe=False)


def updateOrder(request):
    orderId = request.POST['orderId']
    update = Order.objects.get(pk=orderId)
    update.order_CustomerId_id = request.POST['customerId']

    update.lambai_pent = request.POST['lambai_pent']
    update.kamar_pent = request.POST['kamar_pent']
    update.seet_pent = request.POST['seet_pent']
    update.mori_pent = request.POST['mori_pent']
    update.jangh_pent = request.POST['jangh_pent']
    update.jolo_pent = request.POST['jolo_pent']
    update.gothan_pent = request.POST['gothan_pent']
    update.lees_pent = request.POST['lees_pent']
    update.vigat_pent = request.POST['vigat_pent']

    update.lambai_shirt = request.POST['lambai_shirt']
    update.chati_shirt = request.POST['chati_shirt']
    update.bay_shirt = request.POST['bay_shirt']
    update.solder_shirt = request.POST['solder_shirt']
    update.kamar_shirt = request.POST['kamar_shirt']
    update.pech_shirt = request.POST['pech_shirt']
    update.kolar_shirt = request.POST['kolar_shirt']
    update.kaf_shirt = request.POST['kaf_shirt']
    update.vigat_shirt = request.POST['vigat_shirt']

    if request.FILES.get('photo') != None:
        path = update.photo.path
        os.remove(str(path))
        update.photo = request.FILES['photo']

    update.save()

    json_data = serializers.serialize("json", [update])
    return JsonResponse(json_data, safe=False)


def changeStatus(request):
    orderId = request.GET['orderId']
    update = Order.objects.get(pk=orderId)

    if update.status == 'pending':
        update.status = 'done'

    elif update.status == 'done':
        update.status = 'pending'

    update.save()
    json_data = serializers.serialize("json", [update])
    return JsonResponse(json_data, safe=False)
