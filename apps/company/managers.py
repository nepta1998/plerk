from django.db import models
from django.db.models import Q


class CompanyManager(models.Manager):  # pylint: disable=too-few-public-methods
    """ Custom queries for company model"""

    def data_table_filter(self, filter_data, order_by):
        """ general filter from datatable"""
        order = {'customer_name': 'customer__name', '-customer_name': '-customer__name',
                 'user_name': 'user__first_name', '-user_name': '-user__first_name'}
        if order_by in order:
            order_by = order[order_by]
        return self.get_queryset().filter(
            Q(code__icontains=filter_data) |
            Q(customer__name__icontains=filter_data) |
            Q(user__first_name__icontains=filter_data) |
            Q(user__last_name__icontains=filter_data) |
            Q(label_quantity__icontains=filter_data) |
            Q(date__icontains=filter_data)
        ).values().order_by(order_by)