# Generated by Django 4.0.4 on 2022-05-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressyoursalad', '0014_pedido_reservado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='reservado',
            field=models.BooleanField(default=False),
        ),
    ]
