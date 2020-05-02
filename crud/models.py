# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)

class Item(models.Model):
    comp_id = models.IntegerField()
    name = models.CharField(max_length=255)
    carb = models.FloatField()
    fat = models.FloatField()
    suaaer = models.FloatField()
    protein = models.FloatField()
    price = models.FloatField()

class CompOrder(models.Model):
    item_id = models.IntegerField()
    prefer_type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    parent_id = models.IntegerField()

class MainData(models.Model):
    parent_id = models.IntegerField()
    item_id = models.IntegerField()

class DrinkData(models.Model):
    parent_id = models.IntegerField()
    item_id = models.IntegerField()

class DessertData(models.Model):
    parent_id = models.IntegerField()
    item_id = models.IntegerField()

class SideData(models.Model):
    parent_id = models.IntegerField()
    item_id = models.IntegerField()