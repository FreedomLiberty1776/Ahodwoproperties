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
	path('accounts_metrics', views.accounts_metrics, name='accounts_metrics'),
	path('map', views.map, name='map'),
	path('tasks', views.tasks, name='tasks'),
	path('accounts', views.accounts, name='accounts'),
	path('apiOverview', views.apiOverview, name='apiOverview'),
	path('task-list/', views.taskList, name='task-list'),
	path('task-create/', views.taskCreate, name='task-create'),
	path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
	path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
	path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
	path('accounts-list/', views.accountsList, name='accounts-list'),
	path('accounts_stats', views.accounts_stats, name='accounts_stats'),

	
]







