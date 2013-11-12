from django.db import models
from django.db.models.fields import DateTimeField


class DbDateTimeField(DateTimeField):

    use_on_insert = False


class TimeStampModel(models.Model):

    created = DbDateTimeField()
