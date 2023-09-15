from django.db import models

# Create your models here.


class AgeCalculator(models.Model):
    birthday_date = models.DateField(null=True)