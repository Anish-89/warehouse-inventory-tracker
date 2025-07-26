from django.db import models

# Product Master Table
class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

# Stock Transaction Main Table
class StockTransaction(models.Model):
    transaction_type = models.CharField(max_length=10, choices=[('IN', 'In'), ('OUT', 'Out')])
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=50, unique=True)

# Stock Transaction Detail Table
class StockDetail(models.Model):
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

