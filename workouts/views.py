from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Accessories, MuscleAnatomy, Workouts, WorkoutTypes
from .serializers import AccessoriesSerializer, MuscleAnatomySerializer, WorkoutsSerializer, WorkoutTypesSerializer

class AccessoriesViewset(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer
    permission_classes = [permissions.IsAdminUser]

class MuscleAnatomyViewset(viewsets.ModelViewSet):
    queryset = MuscleAnatomy.objects.all()
    serializer_class = MuscleAnatomySerializer
    permission_classes = [permissions.IsAdminUser]

class WorkoutsViewset(viewsets.ModelViewSet):
    queryset = Workouts.objects.all()
    serializer_class = WorkoutsSerializer
    permission_classes = [permissions.IsAdminUser]

class WorkoutTypesViewset(viewsets.ModelViewSet):
    queryset = WorkoutTypes.objects.all()
    serializer_class = WorkoutTypesSerializer
    permission_classes = [permissions.IsAdminUser]