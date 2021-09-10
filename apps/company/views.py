from rest_framework.views import APIView
from rest_framework.response import Response
from apps.transaction.models import Transaction, Company
from apps.company.models import Company

class ReportCompany(APIView):

    def get(self, request, format=None, **kwargs):
        """
        Return 
        """
        company = Company.objects.get(pk=kwargs['pk'])
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