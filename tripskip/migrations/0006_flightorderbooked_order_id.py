# Generated by Django 3.1.2 on 2020-10-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripskip', '0005_flightorderbooked'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightorderbooked',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
