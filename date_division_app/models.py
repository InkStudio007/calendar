from django.db import models


class DateDifference(models.Model):
    from_date = models.CharField(max_length=70)
    to_date = models.CharField(max_length=70)

