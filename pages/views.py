from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pages.models import Properties, Agent, Accounts, Transaction, Service, Property_type, Payment_method
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum, Max
from xhtml2pdf import pisa
import random
import PyPDF2




@login_required
def createinvoice(request):
		# context = {'heading': 'Invoice Form', 'title':'Ahodwoproperties | Invoice'}	
	# if request.user.is_authenticated:
		if request.method == 'POST':
			context = None
			invoice_number = random.randint(100000,999999)
			first= request.POST['first']
			last= request.POST['last']
			address= request.POST['address']
			service= request.POST['service']
			cost= request.POST['cost']
			method= request.POST['method']
			charge= request.POST['charge']
			contact= request.POST['contact']
			location= request.POST['location']
			property_type= request.POST['property_type']
			charged= (int(request.POST['charge'])/100)* int(request.POST['cost'])
			date= request.POST['date']
			agent= request.POST['agent']
			description = request.POST['description']
			charge = (int(request.POST['charge'])/100)* int(request.POST['cost'])
			debit = 0
			credit = float(charge)
			transaction_date = date
			j_description = service +' of '+ property_type+ ': AHP'+ str(invoice_number)
			post_ref = 500
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
			j= Accounts(transaction_ref_no=transaction_ref_no,transaction_date=transaction_date,description=j_description,post_ref=post_ref,debit=debit,credit=credit, balance=balance, agent=agent)
			p = Transaction(charge=charge, invoice_number=invoice_number, first=first, last=last, address=address, location=location, property_type=property_type, service=service, sales_price=cost, percent_charged = charge, payment_method =method, agent=agent, date=date)
			p.save()
			j.save()
			data  = {
			'first': request.POST['first'],
			'last': request.POST['last'],
			'address': request.POST['address'],
			'service': request.POST['service'],
			'cost': request.POST['cost'],
			'method': request.POST['method'],
			'charge': request.POST['charge'],
			'contact': request.POST['contact'],
			'agent': request.POST['agent'],
			'invoice_number': invoice_number,
			'charged': (int(request.POST['charge'])/100)* int(request.POST['cost']),
			'date': request.POST['date'],
			'description': 'Service Charge for '+ service + 'of ' + property_type + ' at ' + location,
			"company": "Ahodwoproperties",
			"phone": "055 3246 573 / 050 461 3609",
			"email": "info@ahodwoproperties.com",
			"website": "Ahodwoproperties.com",
			}
			context = { 'data': data, 'title':'Ahodwoproperties | Invoice'}
			return render(request, 'pages/pdf_template.html', context)
		return redirect('transaction')


@login_required
def properties(request):
	context = {'heading': 'Property Form', 'title':'Ahodwoproperties | Properties'}
	if request.method == 'POST':
		electorial_area = request.POST['electorial_area']
		sub_area = request.POST['sub_area']
		geolocation = request.POST['geolocation']
		description = request.POST['description']
		property_type = request.POST['property_type']
		owner = request.POST['owner']
		contact = request.POST['contact']
		price = request.POST['price']
		image = request.POST['image']
		property_id = request.POST['id']
		director = request.POST['director']
		p = Properties(property_type=property_type, geolocation=geolocation, sub_area=sub_area, electorial_area=electorial_area, description=description, owner=owner, owner_contact=contact, price=price, image=image, property_id=property_id)
		p.save()
		return render(request, 'pages/' + director + '.html', context)
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
	context = {'heading': 'Service Form', 'title':'Ahodwoproperties | Service'}
	if request.method == 'POST':
		service = request.POST['service']
		description = request.POST['description']
		p = Service(service=service, description=description)
		p.save()
	return render(request, 'pages/service.html', context)


@login_required
def property_type(request):
	context = {'heading': 'Property Type Form', 'title':'Ahodwoproperties | Property Type'}
	if request.method == 'POST':
		property_type = request.POST['property_type']
		description = request.POST['description']
		p = Property_type(property_type=property_type, description=description)
		p.save()
	return render(request, 'pages/property_type.html', context)

@login_required
def payment_method(request):
	context = {'heading': 'Payment Method Form', 'title':'Ahodwoproperties | Payment Method'}
	if request.method == 'POST':
		payment_method = request.POST['payment_method']
		description = request.POST['description']
		p = Payment_method(payment_method=payment_method, description=description)
		p.save()
		
	return render(request, 'pages/payment_method.html', context)


@login_required
def transaction(request):
	p = Agent.objects.all()
	k = Service.objects.all()
	t = Property_type.objects.all()
	f = Payment_method.objects.all()
	context = {'heading': 'Invoice Form', 'agent':p, 'service':k, 'property':t, 'method':f, 'title':'Ahodwoproperties | Invoice'}
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
	if Accounts.objects.count() > 0:
		total_debit = float(Accounts.objects.aggregate(Sum('debit'))['debit__sum'])
		total_credit = float(Accounts.objects.aggregate(Sum('credit'))['credit__sum'])
		last_balance = float(total_credit - total_debit)
	else:
		last_balance = None
	accounts_metrics = Accounts.objects.all()
	
	context = {'heading': 'Accounts Metrics', 'accounts_metrics':accounts_metrics, 'last_balance':last_balance, 'title':'Ahodwoproperties | Accounts Metrics'}
	return render(request,'pages/accounts_metrics.html', context)

@login_required
def map(request):
	context = {'heading': 'Map', 'title':'Ahodwoproperties | Map'}
	return render(request, 'pages/map.html', context)

@login_required
def accounts(request):
	context = {'heading': 'Accounts', 'title':'Ahodwoproperties | Accounts'}
	if request.method == 'POST':
		debit = 0
		credit = 0
		transaction_date = request.POST['transaction_date']
		description = request.POST['description']
		post_ref = request.POST['post_ref']
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
		p = Accounts(transaction_ref_no=transaction_ref_no, transaction_date=transaction_date,description=description,post_ref=post_ref,debit=debit,credit=credit, balance=balance, agent=agent)
		p.save()
		return render(request, 'pages/accounts.html', context)
	return render(request, 'pages/accounts.html', context)


