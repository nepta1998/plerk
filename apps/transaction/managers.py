from django.db import models
from django.db.models import Count, Q
from django.db.models.functions import TruncMonth, TruncDay




class TransactionManager(models.Manager):  # pylint: disable=too-few-public-methods
    """ Custom queries for transaction model"""
    
    def company_max_sales(self):
        count=count=Count('company', filter=Q(status_approved=True) & Q(status_transaction = 'closed'))
        max_sale = self.get_queryset().values('company__name').annotate(count = count).order_by('-count')[0]
        return max_sale
    
    def company_min_sales(self):
        count=count=Count('company', filter=Q(status_approved=True) & Q(status_transaction = 'closed'))
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
    
    def total_transactions_charged_by_company(self, company):
        total = self.get_queryset().filter(Q(company = company) & Q(status_approved=True)).count()
        return total
    
    def total_transactions_no_charged_by_company(self, company):
        total = self.get_queryset().filter(Q(company = company) & Q(status_approved=False)).count()
        return total
    
    def day_max_transactions_by_company(self, company):
        count=Count('day', filter=Q(company=company))
        records = self.get_queryset().annotate(day=TruncDay('date')).values('day').annotate(count=count).order_by('-count')
        totales = [records[0]]
        for r in records[1:]:
            if r['count'] == totales[0]['count']:
                totales.append(r)
                continue
            break
        return totales

    def count_transactions_by_company(self, company):
        total = self.get_queryset().filter(company=company).count()
        return total

    def transactions_by_month_company(self, company):
        count=Count('month', filter=Q(company=company))
        months = self.get_queryset().annotate(month=TruncMonth('date')).values('month').annotate(count=count).order_by('month')
        total = self.count_transactions_by_company(company)
        for month in months:
            month['month'] = month['month'].strftime("%B")
            month['percent'] = round(month["count"] / total * 100, 2)
        return months