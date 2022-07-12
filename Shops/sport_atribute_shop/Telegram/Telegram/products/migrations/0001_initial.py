# Generated by Django 4.0.6 on 2022-07-05 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('cost', models.PositiveIntegerField()),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer')),
                ('teg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.teg')),
            ],
        ),
    ]