# Generated by Django 5.0.2 on 2024-02-21 13:27

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('total', models.FloatField()),
                ('troco', models.CharField(blank=True, max_length=20)),
                ('pagamento', models.CharField(max_length=20)),
                ('ponto_referencia', models.CharField(blank=True, max_length=2000)),
                ('data', models.DateTimeField(default=datetime.datetime(2024, 2, 21, 10, 27, 3, 994969))),
                ('cep', models.CharField(blank=True, max_length=50)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=30)),
                ('entregue', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('adicionais', models.TextField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
            ],
        ),
    ]
