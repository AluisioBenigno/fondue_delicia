# Generated by Django 5.0.2 on 2024-02-21 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupomDesconto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('desconto', models.FloatField()),
                ('usos', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 21, 10, 55, 39, 126150)),
        ),
    ]
