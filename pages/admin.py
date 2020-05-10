from django.contrib import admin
from . models import Transaction, Properties, Agent, Service, Payment_method, Property_type



admin.site.register(Transaction)
admin.site.register(Agent)
admin.site.register(Service)
admin.site.register(Payment_method)
admin.site.register(Property_type)
admin.site.register(Properties)
