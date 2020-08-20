

# from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, AccountsSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pages.models import Properties, Agent, Accounts, Transaction, Service, Property_type, Payment_method, Post_Ref, Business
from rest_framework import serializers
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum, Max
from xhtml2pdf import pisa
import random
import json
import PyPDF2


@login_required
def createinvoice(request):
		context = None
		if request.method == 'POST':
			invoice_number = random.randint(100000,999999)
			first= request.POST['first']
			last= request.POST['last']
			address= request.POST['address']
			service= request.POST['service']
			cost= request.POST['cost']
			method = request.POST['method']	
			usd_equi = ''			
			usd_rate = ''
			rate_reference = ''
			charge = request.POST['charge']
			post_ref = request.POST['post_ref']
			business = request.POST['business']
			contact= request.POST['contact']
			location= request.POST['location']
			property_type= request.POST['property_type']
			charged= (int(charge)/100)* int(cost)
			date= request.POST['date']
			agent= request.POST['agent']
			description = request.POST['description']
			transaction_type = 'credit'
			comment = 'None'
			# charge = (int(request.POST['charge'])/100)* int(request.POST['cost'])
			debit = 0
			credit = float(charged)
			transaction_date = date
			j_description = service +' of '+ property_type+ ': AHP'+ str(invoice_number)
			# post_ref = 500
			balance = 0
			if Accounts.objects.count() > 0:
				max_trans_ref_no = Accounts.objects.aggregate(Max('transaction_ref_no'))
				transaction_ref_no = max_trans_ref_no['transaction_ref_no__max'] +1
				total_credit = float(Accounts.objects.aggregate(Sum('credit'))['credit__sum']) + float(credit)
				total_debit = float(Accounts.objects.aggregate(Sum('debit'))['debit__sum'])
				balance = total_credit- total_debit
			else:
				balance = credit - debit
				transaction_ref_no = 10000001
			j= Accounts(usd_equi=usd_equi, usd_rate=usd_rate, rate_reference=rate_reference, transaction_ref_no=transaction_ref_no, transaction_type=transaction_type, business=business, comment=comment, transaction_date=transaction_date,description=description,post_ref=post_ref,debit=debit,credit=credit, balance=balance, agent=agent)
			p = Transaction(charge=charged, invoice_number=invoice_number, first=first, last=last, address=address, location=location, property_type=property_type, service=service, sales_price=cost, percent_charged = charge, payment_method =method, agent=agent, date=date)
			p.save()
			j.save()
			data  = {
			'first': request.POST['first'].capitalize(),
			'last': request.POST['last'].capitalize(),
			'address': request.POST['address'],
			'service': request.POST['service'].capitalize(),
			'cost': request.POST['cost'],
			'method': request.POST['method'].capitalize(),
			'charge': request.POST['charge'],
			'contact': request.POST['contact'],
			'agent': request.POST['agent'],
			'invoice_number': invoice_number,
			'charged': round((int(request.POST['charge'])/100)* int(request.POST['cost']),2), 
			'date': request.POST['date'],
			'description': 'Service Charge for '+ service + 'of ' + property_type + ' at ' + location,
			"company": "Ahodwoproperties",
			"phone": "024 333 2465 / 020 146 3758",
			"email": "info@ahodwoproperties.com",
			"website": "Ahodwoproperties.com",
			}	
			context = {'data': data, 'title': 'Ahodwoproperties | Invoice'}
			return render(request, 'pages/pdf_template.html', context)
		return render(request, 'pages/pdf_template.html', context)


@login_required
def properties(request):
	context = {'heading': 'Property Form', 'title':'Ahodwoproperties | Properties'}
	if request.method == 'POST':
		property_id = request.POST['id']
		director = request.POST['director']
		database = Properties.objects.values_list('property_id', flat=True)
		if property_id in database and property_id !='none' and director == 'properties':
			messages.error(request, 'The house/plot no. "'+property_id+'"'+' already exist in the database' )
			return render(request, 'pages/properties.html', context)
		elif property_id in database and director == 'map':
			messages.error(request, 'The house/plot no. "'+property_id+'"'+' already exist in the database' )
			return redirect('map')
		else:
			electorial_area = request.POST['electorial_area'].lower()
			sub_area = request.POST['sub_area'].lower()
			geolocation = request.POST['geolocation']
			description = request.POST['description'].lower()
			property_type = request.POST['property_type'].lower()
			owner = request.POST['owner'].lower()
			contact = request.POST['contact']
			price = request.POST['price']
			handler = request.POST['handler']
			is_listed = False
			if  'listed' in request.POST:
				is_listed =True
			image = request.POST['image']
			p = Properties(property_type=property_type, geolocation=geolocation, sub_area=sub_area, electorial_area=electorial_area, description=description, owner=owner, handler=handler, is_listed=is_listed, owner_contact=contact, price=price, image=image, property_id=property_id)
			p.save()
			trigger = {}
			trigger['trigger'] = {
				'electorial_area': electorial_area.capitalize(),
				'sub_area': sub_area.capitalize(),
				'geolocation': geolocation,
				'description': description.capitalize(),
				'property_type': property_type.capitalize(),
				'owner': owner.capitalize(),
				'price': price,
				'contact': contact,
				'property_id': property_id,
			}
			trigger = json.dumps(trigger)
			if director == 'map':
				queryset = Properties.objects.all()
				dictionary = {}
				for i in queryset:
					dictionary[i.property_id] = {
						'property_id':i.property_id,
						'electorial_area':i.electorial_area,
						'sub_area':i.sub_area,
						'description':i.description,
						'owner':i.owner,
						'owner_contact':i.owner_contact,
						'property_type': i.property_type,
						'geolocation':i.geolocation,
						'price':str(i.price),
						'date':str(i.date.date())
						}
				data = json.dumps(dictionary)
				context = {'heading': None, 'title': 'Ahodwoproperties | Map', 'data': data}
				context["trigger"]= trigger
				return render(request, 'pages/map.html', context)
			elif director == 'properties':
				context["trigger"]= trigger
				return render(request, 'pages/properties.html', context)
	return render(request, 'pages/properties.html', context)


@login_required
def agent(request):
	context = {'heading': 'Agent Form'}
	if request.method == 'POST':
		first = request.POST['first']
		last = request.POST['last']
		address = request.POST['address']
		contact = request.POST['contact']
		position = request.POST['position']
		agent_id = request.POST['id']
		p = Agent(first=first, last=last, address=address, contact=contact, position=position, agent_id =agent_id)
		p.save()
	return render(request, 'pages/agent.html', context)


@login_required
def service(request):
	context = {'heading': 'Service Form', 'title': 'Ahodwoproperties | Service'}
	if request.method == 'POST':
		service = request.POST['service'].lower()
		description = request.POST['description'].lower()
		database = Service.objects.values_list('service', flat=True)
		if service in database:
			messages.error(request, 'The service "'+service+'"'+' already exist in the database' )
			return render(request, 'pages/service.html', context) 
		p = Service(service=service, description=description)
		p.save()
		trigger = {}
		trigger['trigger'] = {
			'service': service.capitalize(),
			'description':description.capitalize()
		}
		trigger = json.dumps(trigger)
		context["trigger"]= trigger
	return render(request, 'pages/service.html', context)


@login_required
def property_type(request):
	context = {'heading': 'Property Type Form', 'title': 'Ahodwoproperties | Property Type'}
	if request.method == 'POST':
		property_type = request.POST['property_type'].lower()
		description = request.POST['description'].lower()
		database = Property_type.objects.values_list('property_type', flat=True)
		if property_type in database:
			messages.error(request, 'The service "' + property_type + '"' + ' already exist in the database')
			return render(request, 'pages/property_type.html', context)
		p = Property_type(property_type=property_type, description=description)
		p.save()
		trigger = {}
		trigger['trigger'] = {
			'property_type': property_type.capitalize(),
			'description':description.capitalize()
		}
		trigger = json.dumps(trigger)
		context["trigger"]= trigger
		return render(request, 'pages/property_type.html', context)
	return render(request, 'pages/property_type.html', context)


@login_required
def payment_method(request):
	context = {'heading': 'Payment Method Form', 'title':'Ahodwoproperties | Payment Method'}
	if request.method == 'POST':
		payment_method = request.POST['payment_method'].lower()
		description = request.POST['description'].lower()
		database = Payment_method.objects.values_list('payment_method', flat=True)
		if payment_method in database:
			messages.error(request, 'The payment method "' + payment_method.capitalize() + '"' + ' already exist in the database')
			return render(request, 'pages/payment_method.html', context)
		p = Payment_method(payment_method=payment_method, description=description)
		p.save()
		trigger = {}
		trigger['trigger'] = {
			'payment_method': payment_method.capitalize(),
			'description':description.capitalize()
		}
		trigger = json.dumps(trigger)
		context["trigger"]= trigger
		return render(request, 'pages/payment_method.html', context)
	return render(request, 'pages/payment_method.html', context)


@login_required
def transaction(request):
	p = Agent.objects.all()
	k = Service.objects.all()
	t = Property_type.objects.all()
	f = Payment_method.objects.all()
	business = Business.objects.all()
	post_ref = Post_Ref.objects.all()
	context = {'heading': 'Invoice Form', 'agent':p, 'service':k, 'property':t, 'method':f, 'title':'Ahodwoproperties | Invoice', 'business':business,'post_ref':post_ref}
	return render(request, 'pages/transaction.html', context)


@login_required
def dashboard(request):
	return render(request, 'pages/home.html')


@login_required
def transaction_metrics(request):
	transaction_metrics = Transaction.objects.all()
	total = Transaction.objects.aggregate(Sum('charge'))
	context = {'transaction_metrics':transaction_metrics, 'total':total, 'heading':'Transaction Metrics', 'title':'Ahodwoproperties | Transaction Metrics'}
	return render(request,'pages/transaction_metrics.html', context)


@login_required
def property_metrics(request):
	property_metrics = Properties.objects.all()
	context = {'heading': 'property Metrics', 'property_metrics':property_metrics, 'title':'Ahodwoproperties | Property Metrics'}
	return render(request, 'pages/property_metrics.html', context)
	

@login_required
def accounts_metrics(request):
	queryset = Accounts.objects.all()
	accounts_metrics = queryset
	if Accounts.objects.count() > 0:
		credit = [float(i.credit) for i in queryset if "Adu" not in i.agent and float(i.credit)!= 0]
		debit = [float(i.debit) for i in queryset if "Adu" not in i.agent and float(i.debit)!= 0]
		availabe_balance = sum(credit)-sum(debit)
		print(availabe_balance)
		total_debit = float(Accounts.objects.aggregate(Sum('debit'))['debit__sum'])
		total_credit = float(Accounts.objects.aggregate(Sum('credit'))['credit__sum'])
		last_balance = float(total_credit - total_debit)
	else:
		last_balance = None
		availabe_balance = None
	
	
	context = {'heading': 'Accounts Metrics', 'accounts_metrics':accounts_metrics, 'last_balance':last_balance, 'title':'Ahodwoproperties | Accounts Metrics', 'availabe_balance':availabe_balance}
	return render(request,'pages/accounts_metrics.html', context)


@login_required
def map(request):
	queryset = Properties.objects.all()
	dictionary = {}
	for i in queryset:
		dictionary[i.property_id] = {
			'property_id':i.property_id,
			'electorial_area':i.electorial_area,
			'sub_area':i.sub_area,
			'description':i.description,
			'owner':i.owner,
			'owner_contact':i.owner_contact,
			'property_type': i.property_type,
			'geolocation':i.geolocation,
			'price':str(i.price),
			'date':str(i.date.date())
			}
	data = json.dumps(dictionary)
	# print(dictionary)
	context = {'heading': None, 'title':'Ahodwoproperties | Map', 'data':data}
	return render(request, 'pages/map.html', context)


@login_required
def accounts(request):
	business = Business.objects.all()
	post_ref = Post_Ref.objects.all()
	print([i for i in post_ref])
	context = {'heading': 'Accounts', 'title': 'Ahodwoproperties | Accounts', 'business': business, 'post_ref':post_ref}
	if request.method == 'POST':
		debit = 0
		credit = 0
		transaction_date = request.POST['transaction_date']
		description = request.POST['description']
		comment = request.POST['comment']
		post_ref = request.POST['post_ref']
		business = request.POST['business']
		usd_equi = request.POST['usd_equi']
		usd_rate = request.POST['usd_rate']
		rate_reference = request.POST['rate_reference']
		transaction_type = request.POST['transaction_type']
		if transaction_type == 'debit':
			debit = request.POST['amount']
		if transaction_type == 'credit':
			credit = request.POST['amount']
		agent = request.POST['agent']
		balance = 0
		if Accounts.objects.count() > 0:
			max_trans_ref_no = Accounts.objects.aggregate(Max('transaction_ref_no'))
			transaction_ref_no = max_trans_ref_no['transaction_ref_no__max'] +1
			if transaction_type == 'credit':
				total_credit = float(Accounts.objects.aggregate(Sum('credit'))['credit__sum']) + float(credit)
			else:
				total_credit = float(Accounts.objects.aggregate(Sum('credit'))['credit__sum'])
			if transaction_type == 'debit':
				total_debit = float(Accounts.objects.aggregate(Sum('debit'))['debit__sum']) + float(debit)
			else:
				total_debit = float(Accounts.objects.aggregate(Sum('debit'))['debit__sum'])
			balance = total_credit- total_debit
		else:
			balance = float(credit) - float(debit)
			transaction_ref_no = 10000001
		p = Accounts(usd_equi=usd_equi, usd_rate=usd_rate, rate_reference=rate_reference, transaction_ref_no=transaction_ref_no, transaction_type=transaction_type, business=business, comment=comment, transaction_date=transaction_date,description=description,post_ref=post_ref,debit=debit,credit=credit, balance=balance, agent=agent)
		p.save()
		m = ''
		if transaction_type == 'debit':
			m = '-'
		messages.error(request, 'You have succefully added a '+ transaction_type+ ' of ₵'+m+request.POST['amount']+ ' to the account.')
		return render(request, 'pages/accounts.html', context)
	return render(request, 'pages/accounts.html', context)


@login_required
def tasks(request):
	return render (request, 'pages/task.html' )


	
@login_required
def accounts_stats(request):
	return render (request, 'pages/accounts_stats.html' )



@api_view(['GET'])
def apiOverview (request):
	api_urls = {
			'List':'/task-list/',
			'Detail View':'/task-detail/<str:pk>/',
			'Create':'/task-create/',
			'Update':'/task-update/<str:pk>/',
			'Delete':'/task-delete/<str:pk>/',
			}

	return Response (api_urls)


@api_view(['GET'])
def taskList (request):
	tasks = Task.objects.all()
	serializer= TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def taskDetail (request, pk):
	task = Task.objects.get(id=pk)
	serializer= TaskSerializer(task, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate (request):
	serializer= TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate (request, pk):
	task = Task.objects.get(id=pk)
	serializer= TaskSerializer(instance=task, data=request.data)
	if serializer.is_valid():	
		serializer.save()
	return redirect('task-list')



@api_view(['DELETE'])
def taskDelete (request, pk):
	tasks = Task.objects.get(id=pk)
	tasks.delete()
	return Response('Task has been deleted')

@api_view(['GET'])
def accountsList (request):
	accounts = Accounts.objects.all()
	serializer= AccountsSerializer(accounts, many=True)
	return Response(serializer.data)







