# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.transaction.models import Transaction

class SummaryService(APIView):

    def get(self, request, format=None):
        max_sale = Transaction.objects.company_max_sales()
        min_sales = Transaction.objects.company_min_sales()
        total_price_charged = Transaction.objects.total_price_with_charge()
        total_price_no_charged = Transaction.objects.total_price_without_charge()
        max_reject = Transaction.objects.company_max_reject()

        report = {
            'max':max_sale, 
            'min':min_sales,
            'total_price_charged': total_price_charged,
            'total_price_no_charged': total_price_no_charged,
            'max_reject': max_reject
        }
        return Response(report)
