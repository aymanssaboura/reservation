# Generated by Django 3.2.5 on 2022-10-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20221028_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirLineCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airlineName', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
