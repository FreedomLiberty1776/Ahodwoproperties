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
	percent_charged = models.IntegerField()
	payment_method = models.CharField(max_length=50)
	agent = models.CharField(max_length=60)
	date = models.DateTimeField()
	

class Properties(models.Model):
	
	location = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	property_id = models.IntegerField(null=True)
	owner = models.CharField(max_length=50)
	owner_contact = models.IntegerField()
	property_type = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	date = models.DateTimeField(default=datetime.now)
	image = models.ImageField(upload_to='properties/images', null=True)


class Agent(models.Model):
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	contact = models.BigIntegerField()
	position = models.CharField(max_length=50)
	agent_id = models.IntegerField(null=True)



class Service(models.Model):
	service = models.CharField(max_length=50)
	description = models.CharField(max_length=50)


class Property_type(models.Model):
	property_type = models.CharField(max_length=50)
	description = models.CharField(max_length=50)


class Payment_method(models.Model):
	payment_method = models.CharField(max_length=50)
	description = models.CharField(max_length=50, null=True)
	
	 
	