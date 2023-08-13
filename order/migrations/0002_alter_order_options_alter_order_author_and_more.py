# Generated by Django 4.2.3 on 2023-08-10 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0002_alter_medicine_options'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='medicine',
            field=models.ManyToManyField(through='order.OrderItem', to='medicine.medicine', verbose_name='Лекарства'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='medicine.medicine', verbose_name='Лекарства'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Кол-во'),
        ),
    ]
