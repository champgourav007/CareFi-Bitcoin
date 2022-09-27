from . import serializers
from . import models
from rest_framework import viewsets, decorators, permissions
from . import bitcoin
from rest_framework.response import Response


class BitcoinViewSet(viewsets.ModelViewSet):
    queryset = models.Bitcoin.objects.all()
    serializer_class = serializers.BitcoinSerializers


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def getBitcoinPrice(request, currency):
    try:
        if currency == None or currency == "":
            currency = 'inr'
        current_price = bitcoin.getBitcoinCurrentPrice(currency)
        bitcoinData = models.Bitcoin(
            name='Bitcoin',
            price=current_price["bitcoin"][currency],
            currency=currency
        )
        bitcoinData.save()
        return Response(current_price, 200)
    except:
        return Response("Currency is Not valid", 400)


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def getBitcoinPricesByTimestamp(request, currency, from_timestamp, to_timestamp):
    try:
        bitcoin_list = bitcoin.getBitcoinListUsingTimestamp(
            currency, from_timestamp, to_timestamp)
        return Response(bitcoin_list, 200)
    except:
        return Response("Some error Occured!! Please check the route.", 400)
