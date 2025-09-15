from django.urls import path
from .views import classes_view
from ...application.service.classes import ClassesService
from ...infrastructure.sqlite.classes import ClassesRepo

urlpatterns = [
    path("", classes_view(ClassesService(ClassesRepo())))
]
