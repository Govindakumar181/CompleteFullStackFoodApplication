# Generated by Django 3.2.4 on 2021-06-23 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_contact_posting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='posting_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 22, 22, 19, 18, 674551)),
        ),
    ]
