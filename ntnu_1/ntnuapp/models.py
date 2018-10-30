from django.db import models
from collections import namedtuple

from django.db import connection


class AP(models.Model):
    name = models.TextField()
    ap_id = models.IntegerField()

    class Meta:
        db_table = "ap"
