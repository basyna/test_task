# Generated by Django 3.2.16 on 2022-11-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название товара', max_length=80, verbose_name='Название товара')),
                ('description', models.TextField(help_text='Введите описаниние товара', verbose_name='Описание товара')),
                ('price', models.FloatField()),
                ('currency', models.CharField(choices=[('usd', 'Доллар США'), ('aud', 'Доллар Австралия'), ('cny', 'Китайский юань')], default='usd', max_length=20, verbose_name='Валюта покупки')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('currency', models.CharField(choices=[('usd', 'Доллар США'), ('aud', 'Доллар Австралия'), ('cny', 'Китайский юань')], default='usd', max_length=20, verbose_name='Валюта покупки')),
            ],
        ),
    ]
