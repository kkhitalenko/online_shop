from django.core.validators import MinValueValidator
from django.db import models


class Good(models.Model):
    title = models.CharField('название', max_length=64)
    price = models.OneToOneField('Price', on_delete=models.CASCADE,
                                 verbose_name='цена', related_name='good')
    qty = models.PositiveIntegerField('количество')
    barcode = models.CharField('штрихкод', max_length=64, unique=True)
    date_update = models.DateField('дата обновления', auto_now=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,
                             verbose_name='тип', related_name='goods')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title


class Price(models.Model):
    CURRENCIES = {
        'RUB': 'RUB',
        'USD': 'USD',
        'EUR': 'EUR',
    }
    currency = models.CharField('валюта', max_length=3, choices=CURRENCIES)
    value = models.DecimalField('стоимость', max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'

    def __str__(self):
        return f'{self.value} {self.currency}'


class Type(models.Model):
    title = models.CharField('название', max_length=64, unique=True)
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'тип товара'
        verbose_name_plural = 'типы товаров'

    def __str__(self):
        return self.title
