# Generated by Django 3.2.5 on 2022-10-28 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20221028_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotherCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(choices=[('1', 'Airline'), ('2', 'Transport'), ('3', 'Farry'), ('4', 'Hotel'), ('5', 'Visa'), ('6', 'Insurance'), ('7', 'Shipping')], default=1, max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='reservationtransport',
            name='transport_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transportcompany', to='reservation.mothercompany'),
        ),
        migrations.AlterField(
            model_name='reservationairline',
            name='airline_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Airlinecompany', to='reservation.mothercompany'),
        ),
        migrations.DeleteModel(
            name='AirLineCompany',
        ),
    ]
