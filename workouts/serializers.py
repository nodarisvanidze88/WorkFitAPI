from rest_framework.serializers import ModelSerializer
from .models import Accessories, Workouts, WorkoutTypes, MuscleAnatomy

class AccessoriesSerializer(ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'

class WorkoutTypesSerializer(ModelSerializer):
    class Meta:
        model = WorkoutTypes
        fields = '__all__'

class MuscleAnatomySerializer(ModelSerializer):
    class Meta:
        model = MuscleAnatomy
        fields = '__all__'

class WorkoutsSerializer(ModelSerializer):
    workoutType = WorkoutTypesSerializer(many = True)
    targetMuscles = MuscleAnatomySerializer(many = True)
    accessories = AccessoriesSerializer(many = True)
    class Meta:
        model = Workouts
        fields = ["id", "name", "workoutType", "description",
                  "instructions", "duration", "repetition", 
                  "restTime", "targetMuscles", "accessories"]