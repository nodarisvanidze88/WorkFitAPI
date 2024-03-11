from rest_framework.serializers import ModelSerializer
from .models import Accessories, Workouts, WorkoutTypes, MuscleAnatomy

class AccessoriesSerializer(ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['accessories']

class WorkoutTypesSerializer(ModelSerializer):
    class Meta:
        model = WorkoutTypes
        fields = ['workoutType']

class MuscleAnatomySerializer(ModelSerializer):
    class Meta:
        model = MuscleAnatomy
        fields = ['muscleName']

class WorkoutsSerializer(ModelSerializer):
    workoutType = WorkoutTypesSerializer(many = True)
    targetMuscles = MuscleAnatomySerializer(many = True)
    accessories = AccessoriesSerializer(many = True)
    class Meta:
        model = Workouts
        fields = ["id", "name", "workoutType", "description",
                  "instructions", "level", "duration", "repetition", 
                  "restTime", "targetMuscles", "accessories"]