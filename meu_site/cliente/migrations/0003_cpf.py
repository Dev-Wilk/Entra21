# Generated by Django 4.1.1 on 2022-09-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
            ],
        ),
    ]
