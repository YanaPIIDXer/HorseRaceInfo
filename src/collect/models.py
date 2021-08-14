from django.db import models
from django.db.models.deletion import CASCADE


# 競争馬情報
class HorseInfo(models.Model):
    name = models.CharField(max_length=64, blank=False,
                            null=False, unique=True)


# レース情報
class RaceInfo(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=16, blank=False, null=False)
    round = models.IntegerField(blank=False, null=False)
    horces = models.ManyToManyField(HorseInfo, related_name="horces")
