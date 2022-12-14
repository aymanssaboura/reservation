# Generated by Django 3.2.5 on 2022-10-28 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_initial'),
        ('company', '0001_initial'),
        ('bus', '0002_initial'),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bus.bus'),
        ),
        migrations.AddField(
            model_name='trip',
            name='cityFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CITY_FROM', to='trip.location'),
        ),
        migrations.AddField(
            model_name='trip',
            name='cityTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CITY_TO', to='trip.location'),
        ),
        migrations.AddField(
            model_name='trip',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='trip',
            name='driver1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Bus_Driver', to='bus.driver'),
        ),
        migrations.AddField(
            model_name='trip',
            name='driver2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BusDriverHelp', to='bus.driver'),
        ),
        migrations.AddField(
            model_name='location',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flight_trip',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flight_trip',
            name='cityFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CITY_FROM_flight', to='trip.location'),
        ),
        migrations.AddField(
            model_name='flight_trip',
            name='cityTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CITY_TO_flight', to='trip.location'),
        ),
        migrations.AddField(
            model_name='flight_trip',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AddField(
            model_name='flight_trip',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='customer.customer'),
        ),
    ]
