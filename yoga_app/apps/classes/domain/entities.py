import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class YogaClassParams:
    start_time: datetime
    class_level: str
    class_name: str
    max_capacity: int
    location: str


@dataclass
class YogaClass:
    id: uuid.UUID
    start_time: datetime
    class_level: str
    class_name: str
    max_capacity: int
    current_capacity: int
    location: str
