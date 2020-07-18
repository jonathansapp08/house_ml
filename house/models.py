from django.db import models


class House(models.Model):
    area = models.BigIntegerField(null=False)
    fireplace = models.BooleanField(null=False, default=False)
    baths = models.BigIntegerField(null=False)
    floors = models.BigIntegerField(null=False)
    city = models.BigIntegerField(null=False)
    electric = models.BooleanField(null=False, default=False)