from yoga_app.apps.classes.domain.entities import YogaClass
from yoga_app.apps.classes.domain.repositories.repositories import IClassesRepository


class ClassesRepo(IClassesRepository):
    def __init__(self, db):
        self.db = db

    def insert(self, yoga_classes: list[YogaClass]) -> list[YogaClass]:
        #implement me
        return yoga_classes