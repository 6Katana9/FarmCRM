from django.db import models


class Medicine(models.Model):
    name = models.CharField('Наименование', max_length=300, null=True)
    price = models.DecimalField('Цена со скидкой', max_digits=10, decimal_places=2,  default=0, blank=True, null=True)
    measure = models.CharField('Ед. измерения', max_length=10, default='', null=True)
    manufacturer = models.CharField('Производитель', max_length=300, default='', null=True)
    expiration_date = models.DateField('Срок годности', default=None,null=True)

    def __str__(self) -> str:
        return f'{self.name}-->{self.price}'
    

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'
