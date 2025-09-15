import uuid

from yoga_app.apps.classes.domain.entities import YogaClassParams, YogaClass
from yoga_app.apps.classes.domain.repositories.repositories import IClassesRepository
from yoga_app.apps.classes.domain.services.services import IClassesService


class ClassService(IClassesService):
    def __init__(self, classes_repo: IClassesRepository):
        self.classes_repo = classes_repo

    def create_classes(self, yoga_class_params: list[YogaClassParams]) -> list[YogaClass]:
        classes = [
            YogaClass(
                id=uuid.UUID(),
                start_time=p.start_time,
                class_level=p.class_level,
                class_name=p.class_name,
                max_capacity=p.max_capacity,
                current_capacity=p.max_capacity,
                location=p.location,
            ) for p in yoga_class_params]

        # TODO: handle error here
        inserted_classes = self.classes_repo.insert(classes)

        return inserted_classes
