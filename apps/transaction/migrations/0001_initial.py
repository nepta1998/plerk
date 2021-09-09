# Generated by Django 3.2.7 on 2021-09-09 04:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('status_transaction', models.CharField(choices=[('closed', 'cerrado'), ('reserved', 'resevado'), ('pending', 'pendiente')], max_length=8)),
                ('status_approved', models.BooleanField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company')),
            ],
        ),
    ]
