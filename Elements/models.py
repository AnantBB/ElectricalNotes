from django.db import models

# Create your models here.

class wire_spec(models.Model):
    wire_length = models.DecimalField(max_digits = 5, decimal_places = 2)
    cross_section = models.DecimalField(max_digits = 3, decimal_places = 1)
    shape = models.CharField(max_length=15)
    Width_to_thickness_ratio = models.DecimalField(max_digits = 3, decimal_places = 2)
    Radius_of_Chamfer = models.DecimalField(max_digits = 3, decimal_places = 2)
    material = models.CharField(max_length=15, default='copper')
    temperature_coefficient = models.DecimalField(max_digits = 6, decimal_places = 5)
    ambient_temperature = models.DecimalField(max_digits = 3, decimal_places = 1)
    resistance = models.DecimalField(max_digits = 5, decimal_places = 2, default=None)
    dissipation_area = models.DecimalField(max_digits = 5, decimal_places = 2, default=None)
    surface_area = models.DecimalField(max_digits = 5, decimal_places = 2, default=None)
    conductor_weight = models.DecimalField(max_digits = 5, decimal_places = 2, default=None)
    specific_heat = models.DecimalField(max_digits = 5, decimal_places = 3, default=None)
    applied_source = models.CharField(max_length=15)
    source_type = models.CharField(max_length=15)
    peak_source_value = models.DecimalField(max_digits = 4, decimal_places = 1)
    period_of_source_connection = models.DecimalField(max_digits = 4, decimal_places = 2)
    step = models.DecimalField(max_digits = 1, decimal_places = 0)
    frequency = models.DecimalField(max_digits = 3, decimal_places = 1)
    temperature = models.DecimalField(max_digits = 4, decimal_places = 1)
    internal_Energy = models.DecimalField(max_digits = 4, decimal_places = 1)
    hot_Resistance = models.DecimalField(max_digits = 4, decimal_places = 1)