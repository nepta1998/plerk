from django.urls import path
from apps.transaction.views import ReportTransaction

urlpatterns = [
    path('', ReportTransaction.as_view()),
]
