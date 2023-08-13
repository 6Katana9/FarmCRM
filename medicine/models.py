from django.db import models


class Medicine(models.Model):
    name = models.CharField('Наименование', max_length=300)
    measure = models.CharField('Ед. измерения', max_length=10)
    discount_price = models.DecimalField('Цена со скидкой', max_digits=10, decimal_places=2)
    manufacturer = models.CharField('Производитель', max_length=300)
    expiration_date = models.DateField('Срок годности')
    price_without_discount = models.DecimalField('Цена без скидкой', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}-->{self.price_without_discount}'
    

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'
