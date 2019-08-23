# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50, null=False)
    u_phone = models.CharField(max_length=10, null=False)
    u_password = models.CharField(max_length=20, null=False)

class NoteCreated(models.Model):
    n_id = models.AutoField(primary_key=True)
    n_val = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class NoteShared(models.Model):
    s_id = models.AutoField(primary_key=True)
    note = models.ForeignKey(NoteCreated, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_accessType = models.BooleanField(default=False) #true for edit access