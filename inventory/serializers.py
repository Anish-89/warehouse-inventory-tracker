from rest_framework import serializers
from .models import Product, StockTransaction, StockDetail

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDetail
        fields = '__all__'

class StockTransactionSerializer(serializers.ModelSerializer):
    stockdetail_set = StockDetailSerializer(many=True, write_only=True)

    class Meta:
        model = StockTransaction
        fields = ['id', 'transaction_type', 'transaction_date', 'reference_number', 'stockdetail_set']

    def create(self, validated_data):
        details = validated_data.pop('stockdetail_set')
        transaction = StockTransaction.objects.create(**validated_data)
        for detail in details:
            StockDetail.objects.create(transaction=transaction, **detail)
        return transaction
