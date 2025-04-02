from django.db import models

from django.db import models

class Material(models.Model):
    material_name = models.CharField('material_name', primary_key=True, max_length=100)

class compound(models.Model):
    comp_id = models.AutoField(primary_key=True)
    Fuel_type = models.CharField(max_length=100, blank=True, null=True)
    zero_carbon_option = models.CharField(max_length=100, blank=True, null=True)
    Fuel_type_rate = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    Zero_carbon_rate = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    green_premium_fuels = models.CharField(max_length=100, blank=True, null=True)
    market = models.CharField(max_length=100, blank=True, null=True)
