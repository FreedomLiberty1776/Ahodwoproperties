from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('createinvoice', views.createinvoice, name='createinvoice'),
	path('transaction', views.transaction, name='transaction'),
	path('properties', views.properties, name='properties'),
	path('agent', views.agent, name='agent'),
	path('service', views.service, name='service'),
	path('property_type', views.property_type, name='property_type'),
	path('payment_method', views.payment_method, name='payment_method'),
	path('transaction_metrics', views.transaction_metrics, name='transaction_metrics'),
	path('property_metrics', views.property_metrics, name='property_metrics'),
	path('map', views.map, name='map'),


]


