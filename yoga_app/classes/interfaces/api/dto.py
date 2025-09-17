from rest_framework import serializers

from ...domain.entities import YogaClass


class CreateClassResponseDTO(serializers.Serializer):
    id = serializers.UUIDField()
    week_day = serializers.CharField(allow_null=False)
    start_date = serializers.DateField(format="%d-%m-%y", allow_null=False)
    start_hour = serializers.TimeField(format="%H:%M", allow_null=False)
    class_level = serializers.CharField(min_length=3, max_length=40, allow_blank=False)
    class_name = serializers.CharField(min_length=3, max_length=40, allow_blank=False)
    current_capacity = serializers.IntegerField()
    max_capacity = serializers.IntegerField()
    location = serializers.CharField(min_length=5, allow_blank=False)

    @classmethod
    def from_domain(cls, yoga_class: YogaClass) -> "CreateClassResponseDTO":
        return cls({
            "id": yoga_class.id,
            "week_day": translate_week_day_to_polish(yoga_class.start_time.weekday()),
            "start_date": yoga_class.start_time.date(),
            "start_hour": yoga_class.start_time.time(),
            "class_level": yoga_class.class_level,
            "class_name": yoga_class.class_name,
            "current_capacity": yoga_class.current_capacity,
            "max_capacity": yoga_class.max_capacity,
            "location": yoga_class.location,
        })

class CreateClassRequestDTO(serializers.Serializer):
    start_time = serializers.DateTimeField(format="iso-8601", required=True)
    class_level = serializers.CharField(min_length=3, max_length=40, allow_blank=False)
    class_name = serializers.CharField(min_length=3, max_length=40, allow_blank=False)
    max_capacity = serializers.IntegerField(min_value=1, allow_null=False)
    location = serializers.CharField(min_length=5, allow_blank=False)


def translate_week_day_to_polish(week_day: int) -> str:
    days = [
        "poniedziałek",
        "wtorek",
        "środa",
        "czwartek",
        "piątek",
        "sobota",
        "niedziela",
    ]

    try:
        return days[week_day]
    except IndexError:
        raise ValueError("unknown week day")
