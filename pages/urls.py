from django.urls import path
from django.contrib.auth import views as auth_views

from wkhtmltopdf.views import PDFTemplateView
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
	path('metrics', views.metrics, name='metrics'),
	path('map', views.map, name='map'),


]


