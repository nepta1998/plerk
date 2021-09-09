from rest_framework import serializers
from apps.transaction.models import Transaction
from django.db.models import Count, Max, Sum

class TransactionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'company', 'date', 'price', 'status_transaction', 'status_approved')