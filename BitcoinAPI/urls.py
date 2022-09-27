from django.urls import path, include
from . import views

urlpatterns = [
    path('api_auth/', include('rest_framework.urls')),
    path(
        'all/', views.BitcoinViewSet.as_view({'get': 'list'}), name='allBitcoin'),
    path('getCurrentPrice/<currency>/',
         views.getBitcoinPrice, name='currentPrice'),
    path('getBitcoinListByTimestamp/<currency>/<from_timestamp>/<to_timestamp>',
         views.getBitcoinPricesByTimestamp, name='bitcoinList')
]
