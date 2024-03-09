from django.db import models

# In Workout Types need to save types for example, for bodybuilders, for fatburning and so on.
class WorkoutTypes(models.Model):
    workoutType = models.CharField(max_length = 50)

    def __str__(self):
        return self.workoutType


# In this model we can add accessories for workouts, for example dumbbells, and so on.
class Accessories(models.Model):
    accessories = models.CharField(max_length = 200, blank=True, null=True)

    def __str__(self):
        return self.accessories
    

class MuscleAnatomy(models.Model):
    muscleName = models.CharField(max_length = 20)

    def __str__(self):
        return self.muscleName


class Workouts(models.Model):
    name = models.CharField(max_length = 100)
    workoutType = models.ManyToManyField(WorkoutTypes)
    description = models.TextField()
    instructions = models.TextField()
    duration = models.IntegerField()
    repetition = models.CharField(max_length = 20)
    restTime = models.CharField(max_length = 20)
    targetMuscles = models.ManyToManyField(MuscleAnatomy)
    accessories = models.ManyToManyField(Accessories, blank=True)

    def __str__(self):
        return self.name 