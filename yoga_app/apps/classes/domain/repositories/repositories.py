from abc import abstractmethod, ABC

from yoga_app.apps.classes.domain.entities import YogaClass


class IClassesRepository(ABC):
    @abstractmethod
    def insert(self, yoga_classes: list[YogaClass]) -> list[YogaClass]:
        pass

