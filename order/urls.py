from django.urls import path
from . import views

urlpatterns = [

    path('viewOrder/', views.viewOrder, name='viewOrder'),
    path('insertOrder/', views.insertOrder, name='insertOrder'),
    path('deleteOrder/', views.deleteOrder, name='deleteOrder'),
    path('editOrder/', views.editOrder, name='editOrder'),
    path('updateOrder/', views.updateOrder, name='updateOrder'),

]
