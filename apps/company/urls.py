from django.urls import path
from apps.company.views import ServiceCompany, MonthsSummary

urlpatterns = [
    path('<pk>/', ServiceCompany.as_view()),
    path('months/<pk>/', MonthsSummary.as_view())
]