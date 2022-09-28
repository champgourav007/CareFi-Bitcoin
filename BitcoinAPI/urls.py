from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'all/', views.BitcoinViewSet.as_view({'get': 'list'}), name='allBitcoin'),
    path('getCurrentPrice/<str:currency>/',
         views.getBitcoinPrice, name='currentPrice'),
    path('getBitcoinListByTimestamp/<str:currency>/<int:from_timestamp>/<int:to_timestamp>',
         views.getBitcoinPricesByTimestamp, name='bitcoinList'),
    path('api-auth/', include('rest_auth.urls')),
]
