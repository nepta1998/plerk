"""Company model"""
from django.db import models
from apps.company.managers import CompanyManager

class Company(models.Model):
    """ Company model """
    status_company = (("active", "activa" ), ("inactive", "inactiva"))
    name = models.CharField( max_length=50 )
    status = models.CharField( max_length= 8, choices = status_company)
    objects = CompanyManager()

    class Meta:
        db_table = 'Companies'