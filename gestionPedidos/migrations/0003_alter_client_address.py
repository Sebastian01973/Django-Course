# Generated by Django 4.0.5 on 2022-06-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=50, verbose_name='La direccion'),
        ),
    ]