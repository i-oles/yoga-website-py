from django.urls import path
from .views import classes_view
from ...application.service.classes import ClassesService

# classes_repo = ClassesRepo()

urlpatterns = [
    path("", classes_view(ClassesService()))
]
