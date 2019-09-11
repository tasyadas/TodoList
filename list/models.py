# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.end_date)
