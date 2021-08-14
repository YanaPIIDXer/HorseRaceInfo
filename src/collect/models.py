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
                                ("Fukushima", "福島",),
                                ("Nigata", "新潟",),
                                ("Tokyo", "東京",),
                                ("Nakayama", "中山",),
                                ("Chukyo", "中京",),
                                ("Kyoto", "京都",),
                                ("Hanshin", "阪神",),
                                ("Ogura", "小倉",),
                            ))


# レース情報
class RaceInfo(models.Model):
    name = models.CharField(max_length=64, blank=False,
                            null=False, default="race")
    horces = models.ManyToManyField(HorseInfo, related_name="horces")
