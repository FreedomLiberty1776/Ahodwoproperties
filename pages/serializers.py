from rest_framework import serializers

from .models import Task, Accounts


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = "__all__"


class AccountsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accounts
		fields = ["transaction_date", 'description', 'debit', 'credit']