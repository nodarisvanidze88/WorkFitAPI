from django.shortcuts import render
from .models import WorkPlans, Day, Time
from .serializers import WorkPlansSerializer, DaySerializer, TimeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated

class DayViewset(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class TimeViewset(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class WorkPlansViewsets(viewsets.ModelViewSet):
    queryset = WorkPlans.objects.all()
    serializer_class = WorkPlansSerializer
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]