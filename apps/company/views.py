from rest_framework.views import APIView
from rest_framework.response import Response
from apps.transaction.models import Transaction, Company
from apps.company.models import Company

class ReportCompany(APIView):

    def get(self, request, format=None, **kwargs):
        """
        Return 
        """
        print(kwargs['pk'])
        
        return Response('hola mundo')