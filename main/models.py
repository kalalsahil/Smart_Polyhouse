from django.db import models

class readings(models.Model):
    temperature=models.DecimalField(max_digits=5, decimal_places=2)
    humidity=models.DecimalField(max_digits=5, decimal_places=2)
    rainfall=models.DecimalField(max_digits=5, decimal_places=2)
    Nitrogen=models.DecimalField(max_digits=5, decimal_places=2)
    Phosphorus=models.DecimalField(max_digits=5, decimal_places=2)
    Potassium=models.DecimalField(max_digits=5, decimal_places=2)
    ph=models.DecimalField(max_digits=5, decimal_places=2)
    result=models.CharField(max_length=50)