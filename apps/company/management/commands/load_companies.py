import csv
from os import name
from django.core.management import BaseCommand
from apps.company.models import Company

class Command(BaseCommand):
    help = 'Load a transactions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            company_names = { name['company'] for name  in reader if name['company'] }
            Company.objects.bulk_create([ Company(name = name, status= 'active') for name in company_names])