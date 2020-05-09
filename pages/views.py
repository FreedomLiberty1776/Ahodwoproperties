from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pages.models import Properties, Agent, Transaction, Service, Property_type, Payment_method
from django.contrib import messages
from django.http import HttpResponse
from xhtml2pdf import pisa
import random
import PyPDF2




@login_required
def createinvoice(request):
			
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
			
			p = Transaction(charge=charge, invoice_number=invoice_number, first=first, last=last, address=address, location=location, property_type=property_type, service=service, sales_price=cost, percent_charged = charge, payment_method =method, agent=agent, date=date)
			p.save()
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
			return render(request, 'pages/pdf_template.html', {'data': data})
		return redirect('transaction')


@login_required
def properties(request):
	if request.method == 'POST':
		location = request.POST['location']
		description = request.POST['description']
		owner = request.POST['owner']
		contact = request.POST['contact']
		price = request.POST['price']
		image = request.POST['image']
		property_id = request.POST['id']
		p = Properties(location=location, description=location, owner=owner, owner_contact=contact, price=price, image=image, property_id=property_id)
		p.save()
	return render(request, 'pages/properties.html')


@login_required
def agent(request):
	if request.method == 'POST':
		first = request.POST['first']
		last = request.POST['last']
		address = request.POST['address']
		contact = request.POST['contact']
		position = request.POST['position']
		agent_id = request.POST['id']
		p = Agent(first=first, last=last, address=address, contact=contact, position=position, agent_id =agent_id)
		p.save()
	return render(request, 'pages/agent.html')


@login_required
def service(request):
	if request.method == 'POST':
		service = request.POST['service']
		description = request.POST['description']
		p = Service(service=service, description=description)
		p.save()
	return render(request, 'pages/service.html')


@login_required
def property_type(request):
	if request.method == 'POST':
		property_type = request.POST['property_type']
		description = request.POST['description']
		p = Property_type(property_type=property_type, description=description)
		p.save()
	return render(request, 'pages/property_type.html')

@login_required
def payment_method(request):
	if request.method == 'POST':
		payment_method = request.POST['payment_method']
		description = request.POST['description']
		p = Payment_method(payment_method=payment_method, description=description)
		p.save()
	return render(request, 'pages/payment_method.html')


@login_required
def transaction(request):
	p = Agent.objects.all()
	k = Service.objects.all()
	t = Property_type.objects.all()
	f = Payment_method.objects.all()
	return render(request, 'pages/transaction.html', {'agent':p, 'service':k, 'property':t, 'method':f})


@login_required
def dashboard(request):
	return render(request, 'pages/home.html')

def metrics(request):
	transaction_metrics = Transaction.objects.all()
	return render(request,'pages/case_history.html', { 'transaction_metrics':transaction_metrics})



