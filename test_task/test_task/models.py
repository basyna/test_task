from django.db import models

CURRENCY_CHOICES = [
    ('usd', 'Доллар США'),
    ('aud', 'Доллар Австралия'),
    ('cny', 'Китайский юань'),
]


class Item(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='Название товара',
        help_text='Введите название товара'
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Введите описаниние товара'
    )
    price = models.IntegerField(
        default=0
    )
    currency = models.CharField(
        'Валюта покупки',
        max_length=20,
        choices=CURRENCY_CHOICES,
        default='usd',
    )

    def __str__(self):
        return self.name
