import uuid

from ...domain.entities import YogaClassParams, YogaClass
from ...domain.repositories.repositories import IClassesRepository
from ...domain.services.services import IClassesService


class ClassesService(IClassesService):
    def __init__(self, classes_repo: IClassesRepository):
        self.classes_repo = classes_repo
        pass

    def create_classes(self, yoga_class_params: list[YogaClassParams]) -> list[YogaClass]:
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

        # TODO: handle error here
        inserted_classes = self.classes_repo.insert(classes)

        return inserted_classes
