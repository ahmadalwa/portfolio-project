from .models import Product
from rest_framework import serializers



# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['name', 'egprice', 'usdprice', 'uroprice', 'image_url']