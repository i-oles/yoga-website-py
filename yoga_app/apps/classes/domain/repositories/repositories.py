from abc import abstractmethod, ABC

from ...domain.entities import YogaClass


class IClassesRepository(ABC):
    @abstractmethod
    def insert(self, yoga_classes: list[YogaClass]) -> list[YogaClass]:
        pass

