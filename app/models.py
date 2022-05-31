from django.db import models

# Create your models here.

class Storage(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.FloatField()

class Rangesort(models.Model):
    storage1 = models.IntegerField()
    storage2 = models.IntegerField()
    storage3 = models.IntegerField()
    storage4 = models.IntegerField()


class ReadyWeight(models.Model):
    weight1 = models.FloatField()
    weight2 = models.FloatField()
    weight3 = models.FloatField()
    weight4 = models.FloatField()

class ReadyRangesort(models.Model):
    w1result = models.FloatField()
    w2result = models.FloatField()
    w3result = models.FloatField()
    w4result = models.FloatField()











