# Generated by Django 3.0.4 on 2021-06-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210604_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='Your Email', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Your Name', max_length=100),
        ),
    ]