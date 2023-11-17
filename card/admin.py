from django.contrib import admin
from card.models import Card, Country, City

# Register your models here.
admin.site.register({Card, Country, City})