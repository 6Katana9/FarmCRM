# Generated by Django 4.2.3 on 2023-09-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_alter_medicine_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена со скидкой'),
        ),
    ]