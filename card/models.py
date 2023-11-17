from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'countries'

class City(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'

class Card(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=True, blank=True)
    img = models.URLField(null=False)
    days = models.IntegerField(null=False)

    class Meta:
        db_table = 'cards'
