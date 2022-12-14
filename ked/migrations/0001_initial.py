# Generated by Django 3.2.5 on 2022-10-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('ked_date', models.DateTimeField(auto_now_add=True)),
                ('dept', models.PositiveIntegerField(default=0)),
                ('credit', models.PositiveIntegerField(default=0)),
                ('memo', models.TextField()),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('title', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
