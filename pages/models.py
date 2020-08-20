from django.db import models
from datetime import datetime



class Transaction(models.Model):
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	service = models.CharField(max_length=50)
	property_type = models.CharField(max_length=50, null=True)
	location = models.CharField(max_length=50, null=True)
	sales_price = models.IntegerField()
	post_ref = models.IntegerField(null=True)
	business = models.IntegerField(null=True)
	percent_charged = models.IntegerField()
	payment_method = models.CharField(max_length=50)
	agent = models.CharField(max_length=60)
	date = models.DateTimeField()
	invoice_number = models.CharField(max_length=10, null=True)
	charge = models.IntegerField(null=True)
	def __str__(self):
		return 'AHP'+ str(self.invoice_number)

class Properties(models.Model):
	electorial_area = models.CharField(max_length=100)
	sub_area = models.CharField(max_length=100,null=True)
	description = models.CharField(max_length=200)
	property_id = models.CharField(max_length=50, null=True)
	owner = models.CharField(max_length=50)
	geolocation= models.CharField(max_length=50, null=True)
	owner_contact = models.IntegerField()
	property_type = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	date = models.DateTimeField(default=datetime.now)
	# image = models.ImageField(upload_to='properties/images', null=True)
	is_listed = models.BooleanField(default=False)
	handler = models.CharField(max_length=100, null=True)
	def __str__(self):
		return self.property_id

class Agent(models.Model):
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	contact = models.BigIntegerField()
	position = models.CharField(max_length=50)
	agent_id = models.IntegerField(null=True)
	def __str__(self):
		return self.first + ' ' +self.last


class Service(models.Model):
	service = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	def __str__(self):
		return self.service

class Property_type(models.Model):
	property_type = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	def __str__(self):
		return self.property_type


class Payment_method(models.Model):
	payment_method = models.CharField(max_length=50)
	description = models.CharField(max_length=50, null=True)
	def __str__(self):
		return self.payment_method


class Accounts(models.Model):
	date_logged = models.DateTimeField(default=datetime.now)
	transaction_date = models.DateField()
	description = models.CharField(max_length=500)
	comment = models.CharField(max_length=1000, null=True)
	agent = models.CharField(max_length=50)
	post_ref = models.IntegerField()
	usd_equi = models.CharField(max_length=10, null=True)
	usd_rate = models.CharField(max_length=10, null=True)
	rate_reference =models.CharField(max_length=100, null=True)
	business = models.IntegerField(null=True)
	transaction_type = models.CharField(max_length=20, null=True)
	debit= models.DecimalField(max_digits=10,decimal_places=2, null=True)
	credit= models.DecimalField(max_digits=10,decimal_places=2, null=True)
	balance = models.DecimalField(max_digits=10, decimal_places=2)
	transaction_ref_no = models.IntegerField(unique=True)
	def __str__(self):
		return self.description


class Post_Ref(models.Model):
	service_item = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	post_ref = models.IntegerField(unique=True)
	def __str__(self):
		return self.service_item

class Business(models.Model):
	select_status = [
		('Active', 'Active'),
		('Suspended', 'Suspended'),
		('Closed', 'Close')
  ]
	business = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	business_id = models.IntegerField(unique=True)
	start_date = models.DateField(default=datetime.now)
	status = models.CharField(max_length=20,choices=select_status, null=True)
	def __str__(self):
		return self.business


class Search(models.Model):
	name = models.CharField(max_length=100)

class Inquiry(models.Model):
	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=20)
	occupation = models.CharField(max_length=20)
	date_of_request= models.DateField()
	service = models.CharField(max_length=50)
	service_area = models.CharField(max_length=50)
	type_of_property = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	willing_to_pay = models.BigIntegerField()
	willing_to_take = models.BigIntegerField()
	price_per_month = models.BigIntegerField()
	contact = models.BigIntegerField()
	is_married = models.BooleanField(default=False)
	number_seeking_rent = models.IntegerField()
	availability_of_water = models.BooleanField(default=False)
	has_electricity = models.BooleanField(default=False)
	has_shared_meter = models.BooleanField(default=False)
	years_in_advance = models.IntegerField()
	tenant_prefered = models.CharField(max_length=200)
	deal_breaker = models.CharField(max_length=1000)

	

class Task(models.Model):
	task_name = models.CharField(max_length=200)
	added_by = models.CharField(max_length=200)
	task_owner = models.CharField(max_length=200)
	added_on = models.DateTimeField(default=datetime.now)
	complete_by =  models.DateField()
	is_completed = models.BooleanField(default=False)
	def __str__(self):
		return self.task_name

	 




	 
	