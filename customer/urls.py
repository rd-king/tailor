from django.urls import path
from . import views

urlpatterns = [

    path('viewCustomer/', views.viewCustomer, name='viewCustomer'),
    path('insertCustomer/', views.insertCustomer, name='insertCustomer'),
    path('deleteCustomer/', views.deleteCustomer, name='deleteCustomer'),
    path('editCustomer/', views.editCustomer, name='editCustomer'),
    path('updateCustomer/', views.updateCustomer, name='updateCustomer'),

]
