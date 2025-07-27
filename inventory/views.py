from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, StockTransaction, StockDetail
from .serializers import ProductSerializer, StockTransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone

def home_view(request):
    return render(request, 'inventory/home.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer

@api_view(['GET'])
def inventory_summary(request):
    products = Product.objects.all()
    inventory = []

    for product in products:
        stock_in = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
        stock_out = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
        balance = stock_in - stock_out
        inventory.append({
            'product': product.name,
            'sku': product.sku,
            'available_stock': balance
        })

    return Response(inventory)

def transaction_form(request):
    if request.method == 'POST':
        t_type = request.POST['transaction_type']
        ref_no = request.POST['reference_number']
        sku = request.POST['sku']
        qty = int(request.POST['quantity'])

        try:
            product = Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            return render(request, 'inventory/transaction_form.html', {'error': 'Invalid SKU'})

        # Check for OUT transaction and stock sufficiency
        if t_type == 'OUT':
            stock_in = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
            stock_out = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
            available = stock_in - stock_out

            if qty > available:
                return render(request, 'inventory/transaction_form.html', {
                    'error': f'❌ Not enough stock. Only {available} items available.'
                })

        transaction = StockTransaction.objects.create(
            transaction_type=t_type,
            reference_number=ref_no,
            transaction_date=timezone.now()
        )

        StockDetail.objects.create(
            transaction=transaction,
            product=product,
            quantity=qty
        )
        return redirect('/inventory/')

    return render(request, 'inventory/transaction_form.html')

def inventory_page(request):
    products = Product.objects.all()
    inventory = []
    for product in products:
        stock_in = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
        stock_out = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
        balance = stock_in - stock_out
        inventory.append({
            'product': product.name,
            'sku': product.sku,
            'stock_in': stock_in,
            'stock_out': stock_out,
            'available_stock': balance
        })
    return render(request, 'inventory/inventory_view.html', {'inventory': inventory})
