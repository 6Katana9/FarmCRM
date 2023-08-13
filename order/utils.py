# Работа с pandas, конвертация в excel
import pandas as pd

from django.core.mail import EmailMessage
from django.conf import settings

def get_excel(**kwargs):
    data = kwargs
    df = pd.DataFrame({'наименование': data['name'],
                       'ед. измерения': data['measure'],
                       'количество':data['quantity'],
                       'цена со скидкой': data['discount_price'],
                       'сумма': data['summ'],
                       'производитель': data['manufacturer'],
                       'срок годности': data['expiration_date'],
                       'цена без скидки' : data['price_without_discount']
                       })
    df.to_excel(f'order/excel_files/{data["author"].email}.xlsx', index=False)


