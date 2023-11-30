from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

    def get_absolute_url(self):
        return reverse('get_item', args=[str(self.id)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
