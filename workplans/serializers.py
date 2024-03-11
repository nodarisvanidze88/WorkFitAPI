from rest_framework.serializers import ModelSerializer
from .models import WorkPlans, Day, Time
from workouts.serializers import WorkoutsSerializer, WorkoutTypesSerializer

class DaySerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ["day"]


class TimeSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields = ["time"]


class WorkPlansSerializer(ModelSerializer):
    preferred_days = DaySerializer(many=True)
    preferred_times = TimeSerializer(many=True)
    workouts = WorkoutsSerializer(many=True)
    goals = WorkoutTypesSerializer(many=True)
    class Meta:
        model = WorkPlans
        fields = '__all__'