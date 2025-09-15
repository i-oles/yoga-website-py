from ...domain.entities import YogaClass
from ...domain.repositories.repositories import IClassesRepository


class ClassesRepo(IClassesRepository):
    def __init__(self):
        pass

    def insert(self, yoga_classes: list[YogaClass]) -> list[YogaClass]:
        # TODO: implement me
        return yoga_classes
