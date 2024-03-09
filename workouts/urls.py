from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccessoriesViewset,MuscleAnatomyViewset,WorkoutsViewset,WorkoutTypesViewset

router = DefaultRouter()

router.register(r'workout', WorkoutsViewset, basename='workout')
router.register(r'types', WorkoutTypesViewset, basename='types')
router.register(r'muscles', MuscleAnatomyViewset, basename='muscles')
router.register(r'accessories', AccessoriesViewset, basename='accessories')

urlpatterns = [
    path('', include(router.urls)),   
]
