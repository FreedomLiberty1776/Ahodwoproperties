from django.contrib import admin
from . models import Transaction, Business, Post_Ref, Properties, Agent, Service, Payment_method, Property_type, Accounts, Task



admin.site.site_header = 'Ahodwo Homes and Properties'



class TransactionAdmin(admin.ModelAdmin):
	list_display = ( 'invoice_number', 'first', 'last', 'service', 'charge')
	list_display_links = ('invoice_number','first')
	search_fields = ('invoice_number', 'first', 'last', 'service', 'charge')
	list_per_page = 25

class PropertyAdmin(admin.ModelAdmin):
	list_display = ('property_id', 'electorial_area', 'sub_area',  'property_type', 'owner_contact')
	list_display_links = ('property_id','electorial_area')
	search_fields = ('property_id', 'electorial_area', 'sub_area', 'owner', 'Property_type', 'owner_contact')
	list_per_page = 25

class AccountAdmin(admin.ModelAdmin):
	list_display = ('transaction_ref_no', 'description', 'transaction_type', 'business',  'post_ref')
	list_display_links = ('transaction_ref_no','description','transaction_type')
	search_fields = ('transaction_ref_no','description', 'transaction_type', 'business', 'post_ref')
	list_per_page = 25

class BusinessAdmin(admin.ModelAdmin):
	list_display = ('business', 'business_id', 'start_date', 'status')
	list_display_links = ('business','business_id','start_date')
	search_fields = ('business','business_id', 'start_date', 'status')
	list_per_page = 25

class PostRefAdmin(admin.ModelAdmin):
	list_display = ('service_item', 'post_ref')
	list_display_links = ('service_item','post_ref')
	search_fields = ('service_item','post_ref')
	list_per_page = 25


class PaymentMethodAdmin(admin.ModelAdmin):
	list_display = ( 'payment_method', 'description')
	list_display_links = ('payment_method', 'description')
	search_fields = ('payment_method', 'description')
	list_per_page = 25

class ServiceAdmin(admin.ModelAdmin):
	list_display = ( 'service', 'description')
	list_display_links = ('service', 'description')
	search_fields = ('service', 'description')
	exclude = ('description',)
	list_per_page = 25

class PropertyTypeAdmin(admin.ModelAdmin):
	list_display = ( 'property_type', 'description')
	list_display_links = ('property_type', 'description')
	search_fields = ('property_type', 'description')
	list_per_page = 25

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Agent)
admin.site.register(Task)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Payment_method, PaymentMethodAdmin)
admin.site.register(Property_type, PropertyTypeAdmin)
admin.site.register(Properties, PropertyAdmin )
admin.site.register(Post_Ref, PostRefAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Accounts, AccountAdmin)
