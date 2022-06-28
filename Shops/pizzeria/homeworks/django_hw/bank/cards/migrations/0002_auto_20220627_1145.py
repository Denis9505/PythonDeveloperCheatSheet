# Generated by Django 3.2.6 on 2022-06-27 08:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='iban',
            field=models.UUIDField(default=uuid.UUID('bbaecb69-c2de-4d04-907c-9c6ea602d294'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bankcustomer',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('88a731df-8e9a-48dc-b927-a6e5dadcdedb'), primary_key=True, serialize=False),
        ),
    ]
