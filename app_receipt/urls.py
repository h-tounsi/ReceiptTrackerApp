from django.urls import path   
from . import views



urlpatterns = [
    path('', views.receipt_list, name='receipt_list'),
    path('receipt/<int:pk>/', views.receipt_detail, name='receipt_detail'),
    path('receipt/new/', views.receipt_new, name='receipt_new'),
    path('receipt/<int:pk>/edit/', views.receipt_edit, name='receipt_edit'),
    path('receipt/<int:pk>/delete/', views.receipt_delete, name='receipt_delete'),
    path('receipt/delete_selected/', views.receipt_delete_selected, name='receipt_delete_selected')
]
