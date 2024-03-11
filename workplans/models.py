from typing import Iterable
from django.db import models
from accounts.models import UserModel
from workouts.models import Workouts, WorkoutTypes

class Day(models.Model):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=20, choices=DAYS_CHOICES, unique = True)

    def __str__(self):
        return self.day

class Time(models.Model):
    TIME_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]
    time = models.CharField(max_length=20, choices=TIME_CHOICES, unique = True)

    def __str__(self):
        return self.time

class WorkPlans(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female')
    ]
    LEVEL_CHOICES = [
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Advanced','Advanced'),
        ('Master','Master')
    ]
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    workouts = models.ManyToManyField(Workouts)
    gender = models.CharField(max_length = 10, choices=GENDER_CHOICES, blank = True, default ="")
    age = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    goals = models.ManyToManyField(WorkoutTypes)
    level = models.CharField(max_length = 15, choices=LEVEL_CHOICES, blank = True, default ="")
    preferred_days = models.ManyToManyField(Day)
    preferred_times = models.ManyToManyField(Time)

    def calculate_bmi(self):
        height_in_meters = self.height/100
        if height_in_meters > 0 and self.weight >0:
            self.bmi = round(self.weight / (height_in_meters ** 2),2)
        else:
            self.bmi = None
    
    def save(self, *args, **kwargs):
        self.calculate_bmi()
        return super().save(*args, **kwargs)