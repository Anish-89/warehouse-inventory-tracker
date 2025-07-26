from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home_view,ProductViewSet, StockTransactionViewSet, inventory_summary,transaction_form,inventory_page

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('transactions', StockTransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home_view),
    path('api/inventory/', inventory_summary),
    path('transaction/', transaction_form),
    path('inventory/', inventory_page),
]
