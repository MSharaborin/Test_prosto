from django.urls import reverse
from django.db import models


class Order(models.Model):
    """
    Таблица заказов.
    """
    number_order = models.AutoField(primary_key=True)
    date_order = models.DateField(auto_now_add=True, verbose_name='Date order',)
    price_order = models.DecimalField(verbose_name='Summary order', max_digits=10, decimal_places=2)
    contractor = models.CharField(max_length=255, verbose_name='Contractor',)
    description = models.TextField(verbose_name='Description order',)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Ordering'

    def __str__(self):
        return self.number_order

    def get_absolute_url(self):
        return reverse('detail_url', args=[str(self.pk)])
