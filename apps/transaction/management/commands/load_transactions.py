from os import name
from apps.company.models import Company
import csv
from django.core.management import BaseCommand
from apps.transaction.models import Transaction
from apps.company.models import Company

validate = {
    'true': True,
    'false': False
}

class Command(BaseCommand):
    help = 'Load a transactions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.DictReader(f, dialect='excel')
            transactions = []
            for q in reader:
                if q['company']:
                    company= Company.objects.get(name=q['company'])
                    del q['company']
                    status_approved = validate[q['status_approved']]
                    del q['status_approved']
                    transactions.append(Transaction(company=company, status_approved= status_approved, **q))
            Transaction.objects.bulk_create(transactions)