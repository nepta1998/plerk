# Generated by Django 3.2.7 on 2021-09-09 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='empresa',
        ),
        migrations.AddField(
            model_name='transaction',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company'),
            preserve_default=False,
        ),
    ]
