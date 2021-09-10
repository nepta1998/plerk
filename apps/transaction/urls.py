from django.urls import path
from apps.transaction.views import SummaryService

urlpatterns = [
    path('', SummaryService.as_view()),
]
