from rest_framework import serializers
from card.models import Card, City, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = ['name', 'country']

class CardSerializer(serializers.Serializer):
    city = CitySerializer()
    score = serializers.DecimalField(max_digits=2, decimal_places=1)
    price = serializers.IntegerField()
    discount = serializers.IntegerField()
    img = serializers.URLField()
    days = serializers.IntegerField()

    class Meta:
        model = Card
        fields = ['id', 'city', 'score', 'price', 'discount', 'img', 'days']