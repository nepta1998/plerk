
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ReportCompany(APIView):

    def get(self, request, format=None):
        """
        Return 
        """
        
        return Response('hola mundo')

class ReportTransaction(APIView):

    def get(self, request, format=None):
        """
        Return 
        """
        
        return Response('hola mundo')