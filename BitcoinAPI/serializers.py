from rest_framework import serializers
from .models import Bitcoin

class BitcoinSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        exclude = ['id']