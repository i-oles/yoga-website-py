import uuid
from datetime import timezone

from django.utils import timezone

from ...domain.entities import YogaClassParams, YogaClass
from ...domain.exceptions import BusinessError
from ...domain.repositories.repositories import IClassesRepository
from ...domain.services.services import IClassesService


class ClassesService(IClassesService):
    def __init__(self, classes_repo: IClassesRepository):
        self.classes_repo = classes_repo
        pass

    def create_classes(self, yoga_class_params: list[YogaClassParams]) -> list[YogaClass]:
        validate_params(yoga_class_params)

        classes = [
            YogaClass(
                id=uuid.uuid4(),
                start_time=p.start_time,
                class_level=p.class_level,
                class_name=p.class_name,
                max_capacity=p.max_capacity,
                current_capacity=p.max_capacity,
                location=p.location,
            ) for p in yoga_class_params]

        inserted_classes = self.classes_repo.insert(classes)

        return inserted_classes


def validate_params(yoga_class_params: list[YogaClassParams]):
    for param in yoga_class_params:
        if param.start_time < timezone.now():
            raise BusinessError(
                message=f"Cannot create class in the past (start_time={param.start_time})",
                code="class_in_past",
            )

    return
