from django.contrib import admin
from .models import Accessories, Workouts, WorkoutTypes, MuscleAnatomy
# Register your models here.

admin.site.register([Accessories, Workouts, WorkoutTypes, MuscleAnatomy])