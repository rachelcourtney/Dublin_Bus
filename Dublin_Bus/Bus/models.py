from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Route(models.Model):
    route_id = models.CharField(primary_key=True, max_length=100)
    agency_id = models.TextField(blank=True, null=True)
    route_short_name = models.TextField(blank=True, null=True)
    route_long_name = models.TextField(blank=True, null=True)
    route_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'



class Calendar(models.Model):
    service_id = models.CharField(primary_key=True, max_length=225)
    monday = models.IntegerField(blank=True, null=True)
    tuesday = models.IntegerField(blank=True, null=True)
    wednesday = models.IntegerField(blank=True, null=True)
    thursday = models.IntegerField(blank=True, null=True)
    friday = models.IntegerField(blank=True, null=True)
    saturday = models.IntegerField(blank=True, null=True)
    sunday = models.IntegerField(blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'


class CalendarDate(models.Model):
    service_id = models.ForeignKey(Calendar, db_column='service_id', on_delete=models.CASCADE)
    date = models.IntegerField(blank=True, null=True)
    exception_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_dates'
        unique_together = (( 'service_id', 'date'))





class Stop(models.Model):
    stop_id = models.CharField(primary_key=True, max_length=100)
    stop_name = models.CharField(blank=True, null=True, max_length=225)
    stop_lat = models.FloatField(blank=True, null=True)
    stop_lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stops'

class Shape(models.Model):
    shape_id = models.CharField(primary_key=True, max_length=225)
    shape_pt_lat = models.FloatField(blank=True, null=True)
    shape_pt_lon = models.FloatField(blank=True, null=True)
    shape_pt_sequence = models.IntegerField(blank=True, null=True)
    shape_dist_traveled = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'

class Trip(models.Model):
    route_id = models.ForeignKey(Route, db_column='route_id', on_delete=models.CASCADE)
    service_id = models.ForeignKey(Calendar, db_column='service_id', on_delete=models.CASCADE)
    trip_id = models.CharField(primary_key=True, max_length=225)
    shape_id = models.ForeignKey(Shape, db_column='shape_id', on_delete=models.CASCADE)
    trip_headsign = models.TextField(blank=True, null=True)
    direction_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'


class StopTime(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    trip_id = models.ForeignKey(Trip, db_column='trip_id', on_delete=models.CASCADE)
    arrival_time = models.TextField()
    stop_id = models.ForeignKey(Stop, db_column='stop_id', on_delete=models.CASCADE)
    stop_sequence = models.IntegerField(blank=True, null=True)
    stop_headsign = models.CharField(blank=True, null=True, max_length=225)
    route_id = models.TextField(blank=True, null=True)
    route_short_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stop_times'
        unique_together = (('trip_id', 'stop_sequence'))







