# Generated by Django 3.2.16 on 2022-10-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_city_state_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.userprofile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('in_print', 'In_Print'), ('out_for_shipment', 'Out_For_shipment')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_type', models.ManyToManyField(to='cart.Type')),
                ('products', models.ManyToManyField(to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.userprofile')),
            ],
        ),
    ]
