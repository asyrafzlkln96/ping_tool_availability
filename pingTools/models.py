from django.db import models
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class DataTerminals(models.Model):
    id = models.AutoField(primary_key=True)
    switch = models.CharField(max_length=50, blank=True, null=True)
    terminal_1 = models.IntegerField(blank=True, null=True)
    terminal_2 = models.IntegerField(blank=True, null=True)
    terminal_3 = models.IntegerField(blank=True, null=True)
    terminal_4 = models.IntegerField(blank=True, null=True)
    terminal_5 = models.IntegerField(blank=True, null=True)
    switch_status = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_terminals'
