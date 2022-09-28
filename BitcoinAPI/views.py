from . import serializers
from . import models
from rest_framework import viewsets, decorators, permissions
from . import bitcoin
from rest_framework.response import Response
from django.shortcuts import render


def home(request):
    return render(request, 'BitcoinAPI/home.html', context={
        "currency": 'inr',
        "from_timestamp": 1605096000,
        "to_timestamp": 1605098000,
    })

# This will give all the Data into the Database


class BitcoinViewSet(viewsets.ModelViewSet):
    queryset = models.Bitcoin.objects.all()
    serializer_class = serializers.BitcoinSerializers

# This will provide the Current Price of the Bitcoin


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
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


# This will Get the result accourding to the timestamp
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def getBitcoinPricesByTimestamp(request, currency, from_timestamp, to_timestamp):
    try:
        bitcoin_list = bitcoin.getBitcoinListUsingTimestamp(
            currency, from_timestamp, to_timestamp)
        return Response(bitcoin_list, 200)
    except:
        return Response("Some error Occured!! Please check the route.", 400)
