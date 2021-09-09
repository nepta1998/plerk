from django.urls import path, include
from rest_framework import routers
from apps.transaction.views import ReportCompany, ReportTransaction

"""ROUTER = routers.DefaultRouter()
ROUTER.register("projects", ProyectoModelViewset)
ROUTER.register("reunion", ReunionModelViewset)"""
urlpatterns = [
    path('transaction/', ReportTransaction.as_view()),
    path('company/', ReportCompany.as_view())
]
