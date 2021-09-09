from apps.company.models import Company
from django.db import models
from django.db.models import Count, Q




class TransactionManager(models.Manager):  # pylint: disable=too-few-public-methods
    """ Custom queries for transaction model"""

    def company_most_sales(self):
        companies = Company.objects.all()
        total = []
        for company in companies:
            transaction = self.get_queryset().filter(status_approved=True, status_transaction = 'closed', company=company).aggregate(count=Count('company'))
            transaction['name'] = company.name
            total.append(transaction)
        return total
    
    def company_most_sales2(self):
        transactions = self.get_queryset().filter(status_approved=True)
        dic = {}
        for transaction in transactions:
            key =  transaction.company.name
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        print(len(dic))
        return dic
    
    def company_max_sales(self):
        count=count=Count('company', filter=Q(status_approved=True, status_transaction = 'closed'))
        max_sale = self.get_queryset().values('company__name').annotate(count = count).order_by('-count')[0]
        return max_sale
    
    def company_min_sales(self):
        count=count=Count('company', filter=Q(status_approved=True, status_transaction = 'closed'))
        min_sale = self.get_queryset().values('company__name').annotate(count = count).order_by('count')[0]
        return min_sale

    def total_price_with_charge(self):
        transactions = self.get_queryset().all()
        price = sum([transaction.convert_cent_usd() for transaction in transactions if transaction.is_charged()])
        return price
    
    def total_price_without_charge(self):
        transactions = self.get_queryset().all()
        price = sum([transaction.convert_cent_usd() for transaction in transactions if not transaction.is_charged()])
        return price
    
    def company_max_reject(self):
        count=Count('company', filter=Q(status_approved=False))
        max_reject = self.get_queryset().values('company__name').annotate(count = count).order_by('-count')[0]
        return max_reject