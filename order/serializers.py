from rest_framework import serializers

from .models import Order, OrderItem
from .utils import get_excel
from .bot import send_excel

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['medicine', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_sum', 'items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        print(items[0]['medicine'].name) #аскорбинка
        validated_data['author'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        order_items = []
        item_name = []
        item_quantity = []
        item_measure = []
        item_discount_price = []
        item_sum = []
        item_manufacturer = []
        item_expiration_date = []
        item_price_without_discount = []

        for item in items:
            order_items.append(
                OrderItem(order=order,
                        medicine=item['medicine'],
                        quantity=item['quantity']
            ))
            item_name.append(item['medicine'].name)
            item_quantity.append(item['quantity'])
            item_measure.append(item['medicine'].measure)
            item_discount_price.append(item['medicine'].discount_price)
            item_sum.append(item['medicine'].price_without_discount * item['quantity'])
            item_manufacturer.append(item['medicine'].manufacturer)
            item_expiration_date.append(item['medicine'].expiration_date)
            item_price_without_discount.append(item['medicine'].price_without_discount)
            total_sum += item['medicine'].price_without_discount * item['quantity']

        OrderItem.objects.bulk_create(order_items)
        order.total_sum = total_sum
        order.save()
        get_excel(name = item_name, measure = item_measure, quantity = item_quantity, discount_price=item_discount_price, summ=item_sum, manufacturer=item_manufacturer, expiration_date=item_expiration_date, price_without_discount=item_price_without_discount, author = self.context['request'].user)
        send_excel(f'order/excel_files/{self.context["request"].user}.xlsx', self.context["request"].user)
        
       
        return order

