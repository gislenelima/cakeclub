# Generated by Django 2.0.5 on 2018-05-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakepage', '0003_auto_20180514_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
        ),
    ]
