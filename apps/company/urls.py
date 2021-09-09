from django.urls import path
from apps.company.views import ReportCompany

urlpatterns = [
    path('<pk>/', ReportCompany.as_view())
]