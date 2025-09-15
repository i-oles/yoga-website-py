import json
from datetime import timezone
from django.http import JsonResponse
from ...domain.entities import YogaClassParams
from ...domain.services.services import IClassesService
from ...interfaces.api.dto import CreateClassRequestDTO, CreateClassResponseDTO
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def classes_view(classes_service: IClassesService):
    @csrf_exempt
    @require_POST
    def create_classes(request):
        try:
            json_body = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "invalid JSON"}, status=400)

        params: list[YogaClassParams] = []

        for c in json_body:
            serializer = CreateClassRequestDTO(data=c)
            if not serializer.is_valid():
                return JsonResponse({"error": "serialization failed"}, status=400)

            param = YogaClassParams(
                start_time=serializer.validated_data["start_time"].astimezone(timezone.utc),
                class_level=serializer.validated_data["class_level"],
                class_name=serializer.validated_data["class_name"],
                max_capacity=serializer.validated_data["max_capacity"],
                location=serializer.validated_data["location"],
            )

            params.append(param)

        # TODO: find the best way for handling handler errors in django
        inserted_classes = classes_service.create_classes(params)

        resp = [CreateClassResponseDTO.from_domain(c).data for c in inserted_classes]

        return JsonResponse({"classes": resp})

    return create_classes
