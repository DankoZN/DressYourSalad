# Generated by Django 4.0.4 on 2022-05-20 21:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dressyoursalad', '0018_alter_pedido_reservado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_carrito', models.IntegerField(default=0, verbose_name='ID Carrito')),
                ('fecha_ped', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('pagado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('boleta', models.IntegerField(default=0, verbose_name='Número de boleta')),
                ('precio', models.IntegerField(default=0, verbose_name='Precio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]