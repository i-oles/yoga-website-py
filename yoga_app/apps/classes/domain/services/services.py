from abc import abstractmethod, ABC

from ...domain.entities import YogaClassParams, YogaClass


class IClassesService(ABC):
    @abstractmethod
    def create_classes(self, yoga_class_params: list[YogaClassParams]) -> list[YogaClass]:
        pass
