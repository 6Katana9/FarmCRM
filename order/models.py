from django.db import models
from django.contrib.auth import get_user_model

from medicine.models import Medicine

User = get_user_model()


class Order(models.Model):
    author = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='Заказчик')
    medicine = models.ManyToManyField(
        Medicine, through='OrderItem', verbose_name='Лекарства'
    )
    total_sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    created_at = models.DateField('Время заказа', auto_now_add=True)

    def __str__(self):
        return f'Order ID: {self.pk} --> {self.created_at} --> {self.author}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey( Order,
                              on_delete=models.CASCADE,
                              related_name='items', verbose_name='Заказ'
                              )
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE,
        related_name='order_item', verbose_name='Лекарства'
    )
    quantity = models.PositiveIntegerField('Кол-во',
        default=1
    )


