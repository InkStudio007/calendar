from django.db import models
# Create your models here.


class DateConversion(models.Model):
    type_status = (
        ('persian to international', 'persian to international'),
        ('international to persian', 'international to persian'),
    )
    international_month_status = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )
    persian_month_status = (
        (1, 'فروردین'),
        (2, 'اردیبهشت'),
        (3, 'خرداد'),
        (4, 'تیر'),
        (5, 'مرداد'),
        (6, 'شهریور'),
        (7, 'مهر'),
        (8, 'آبان'),
        (9, 'آذر'),
        (10, 'دی'),
        (11, 'بهمن'),
        (12, 'اسفند')
    )
    conversion_type = models.CharField(max_length=200, choices=type_status, default='international_to_persian', null=True)
    year = models.IntegerField(null=True)
    international_month = models.PositiveSmallIntegerField(choices=international_month_status, default=1, null=True)
    persian_month = models.PositiveSmallIntegerField(choices=persian_month_status, default=1, null=True)
    day = models.IntegerField(null=True)



