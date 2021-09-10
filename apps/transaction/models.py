""" model Trasaction"""
from django.db import models
from apps.company.models import Company
import uuid
from apps.transaction.managers import TransactionManager

class Transaction(models.Model):
    """model Transaction """
    status = (("closed", "cerrado"), ("reserved", "resevado"), ("pending", "pendiente"))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete = models.PROTECT)
    date = models.DateTimeField()
    price = models.FloatField()
    status_transaction = models.CharField(max_length = 8, choices = status)
    status_approved = models.BooleanField()
    objects = TransactionManager()
    
    class Meta:
        db_table = 'Transactions'

    def is_charged(self):
        """ validate end charged """
        return self.status_transaction == "closed" and self.status_approved
    
    def convert_cent_usd(self):
        return self.price / 100
    
