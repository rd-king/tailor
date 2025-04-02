from django.urls import path
from . import views

urlpatterns = [

    path('viewMeasurement/', views.viewMeasurement, name='viewMeasurement'),
    path('insertMeasurement/', views.insertMeasurement, name='insertMeasurement'),
    path('deleteMeasurement/', views.deleteMeasurement, name='deleteMeasurement'),
    path('editMeasurement/', views.editMeasurement, name='editMeasurement'),
    path('updateMeasurement/', views.updateMeasurement, name='updateMeasurement'),

    path('insertOrder/', views.insertOrder, name='insertOrder'),
    path('deleteOrder/', views.deleteOrder, name='deleteOrder'),
    path('editOrder/', views.editOrder, name='editOrder'),
    path('updateOrder/', views.updateOrder, name='updateOrder'),

    path('changeStatus/', views.changeStatus, name='changeStatus'),

]
