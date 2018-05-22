# Generated by Django 2.0.5 on 2018-05-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakepage', '0002_auto_20180514_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuplaDaVez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_um', models.CharField(max_length=50)),
                ('nome_dois', models.CharField(max_length=50)),
                ('date_da_dupla', models.DateField(verbose_name='Data da dupla')),
            ],
        ),
        migrations.DeleteModel(
            name='DuplasDaVez',
        ),
    ]
