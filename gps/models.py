# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models


class UserPosition(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    latitude = models.FloatField(default=None, null=True)
    longitude = models.FloatField(default=None, null=True)
