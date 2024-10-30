from django.db import transaction
from rest_framework import serializers

from goods.models import Good, Price, Type


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('value', 'currency')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('title', 'description')


class GoodSerializer(serializers.ModelSerializer):
    price = PriceSerializer()
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='title')

    class Meta:
        model = Good
        fields = ('id', 'title', 'price', 'qty', 'barcode', 'type')
        read_only_fields = ('id',)

    @transaction.atomic()
    def create(self, validated_data):
        price = validated_data.pop('price')
        currency = price['currency']
        value = price['value']
        price_obj = Price.objects.create(currency=currency, value=value)
        good_obj = Good.objects.create(price=price_obj, **validated_data)
        return good_obj

    @transaction.atomic()
    def update(self, instance, validated_data):
        price = validated_data.pop('price')
        price_obj = instance.price
        price_obj.currency = price['currency']
        price_obj.value = price['value']
        price_obj.save()

        instance.price = price_obj
        instance.title = validated_data.pop('title')
        instance.qty = validated_data.pop('qty')
        instance.barcode = validated_data.pop('barcode')
        instance.type = validated_data.pop('type')
        instance.save()

        return instance


class ReduceSerializer(serializers.Serializer):
    value = serializers.IntegerField(
        help_text='Число, на которое необходимо уменьшить количество товаров'
    )

    def validate_value(self, value):
        cur_qty = self.context['good'].qty

        if value > cur_qty:
            raise serializers.ValidationError(f'Число должно быть меньше {cur_qty}')
        return value
