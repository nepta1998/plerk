from rest_framework.views import APIView
from rest_framework.response import Response
from apps.transaction.models import Transaction, Company
from apps.company.models import Company
from django.shortcuts import get_object_or_404

class ServiceCompany(APIView):

    def get(self, request, format=None, **kwargs):
        company = get_object_or_404(Company, pk=kwargs['pk'])
        charged = Transaction.objects.total_transactions_charged_by_company(company)
        no_charged = Transaction.objects.total_transactions_no_charged_by_company(company)
        max_transactions=Transaction.objects.day_max_transactions_by_company(company)

        dic = {
            'name': company.name,
            'charged': charged,
            'no_charged': no_charged,
            'max_transactions': max_transactions
        }
        
        return Response(dic)

class MonthsSummary(APIView):

    def get(self, request, format=None, **kwargs):
        company = Company.objects.get(pk=kwargs['pk'])
        total = Transaction.objects.count_transactions_by_company(company)
        months = Transaction.objects. transactions_by_month_company(company)
        max_month = max(months, key=lambda x:x['count'])
        min_month = min(months, key=lambda x:x['count'])
        dic = {
            'name': company.name,
            'total': total,
            'months': months,
            'max': max_month,
            'min': min_month
        }
        
        return Response(dic)