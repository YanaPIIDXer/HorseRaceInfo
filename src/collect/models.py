from django.db import models
from django.db.models.deletion import CASCADE


# 競争馬情報
class HorseInfo(models.Model):
    name = models.CharField(max_length=64, blank=False,
                            null=False, unique=True)


# 開催場所情報
class CourseInfo(models.Model):
    name = models.CharField(max_length=32, blank=False,
                            null=False, unique=True, choices=(
                                ("Sapporo", "札幌",),
                                ("Hakodate", "函館",),
                                ("Sapporo", "福島",),
                                ("Sapporo", "新潟",),
                                ("Sapporo", "東京",),
                                ("Sapporo", "中山",),
                                ("Sapporo", "中京",),
                                ("Sapporo", "京都",),
                                ("Sapporo", "阪神",),
                                ("Sapporo", "小倉",),
                            ))


# レース情報
class RaceInfo(models.Model):
    date = models.DateField()
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    round = models.IntegerField(blank=False, null=False)
    horces = models.ManyToManyField(HorseInfo, related_name="horces")
