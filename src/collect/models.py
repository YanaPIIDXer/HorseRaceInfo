from django.db import models


# レース情報
class RaceInfo(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=16, blank=False, null=False)
    round = models.IntegerField(blank=False, null=False)
