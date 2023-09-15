from django.db import models


class DateDifference(models.Model):
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

