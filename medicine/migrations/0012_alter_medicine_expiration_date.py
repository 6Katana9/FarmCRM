# Generated by Django 4.2.3 on 2023-09-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0011_alter_medicine_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiration_date',
            field=models.DateField(default=None, null=True, verbose_name='Срок годности'),
        ),
    ]
