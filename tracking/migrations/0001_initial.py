# Generated by Django 4.1.6 on 2023-04-03 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_country_state_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_no', models.CharField(default='220116850915', max_length=12, unique=True)),
                ('tracking_description', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('quantity', models.CharField(max_length=100)),
                ('delivered', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100, null=True)),
                ('estdeliveryDate', models.DateTimeField(auto_now=True)),
                ('shipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipment_key', to='authentication.shipment')),
                ('shipping_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shippingfrom_key', to='authentication.shippingfrom')),
                ('shipping_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shippingto_key', to='authentication.shippingto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
    ]
