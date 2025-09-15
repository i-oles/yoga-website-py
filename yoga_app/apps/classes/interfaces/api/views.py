import json
from datetime import timezone

from django.http import JsonResponse
from django.views import View

from yoga_app.apps.classes.domain.entities import YogaClassParams
from yoga_app.apps.classes.domain.services.services import IClassesService
from yoga_app.apps.classes.interfaces.api.dto import CreateClassRequestDTO, CreateClassResponseDTO


class ClassView(View):
    def __init__(self, classes_service: IClassesService):
        super().__init__()
        self.classesService = classes_service

    def post(self, request):
        try:
            json_body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid JSON"}, status=400)

        params: list[YogaClassParams] = []

        for c in json_body:
            serializer = CreateClassRequestDTO(data=c)
            if not serializer.is_valid():
                return JsonResponse({"error": "serialization failed"}, status=400)

            param = YogaClassParams(
                start_time=serializer.start_time.astimezone(timezone.utc),
                class_level=serializer.class_level,
                class_name=serializer.class_name,
                max_capacity=serializer.max_capacity,
                location=serializer.location,
            )

            params.append(param)

        #TODO: find the best way for handling handler errors in django
        inserted_classes = self.classesService.create_classes(params)

        resp = [CreateClassResponseDTO.from_domain(c) for c in inserted_classes]

        return JsonResponse({"classes": resp})
