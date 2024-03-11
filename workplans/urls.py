from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkPlansViewsets, DayViewset, TimeViewset

router = DefaultRouter()

router.register(r'workplans', WorkPlansViewsets, basename='workplans')
router.register(r'day', DayViewset, basename='day')
router.register(r'time', TimeViewset, basename='time')

urlpatterns = [
    path('', include(router.urls)),

]
