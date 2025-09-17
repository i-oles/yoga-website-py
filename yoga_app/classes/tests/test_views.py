import datetime
import uuid
import pytest
from datetime import timedelta
from unittest.mock import MagicMock, patch
from django.test import Client
from django.urls import path
from yoga_app.classes.domain.entities import YogaClass
from yoga_app.classes.interfaces.api.views import classes_view

test_class_id = uuid.uuid4()
test_future_date = datetime.datetime.now() + timedelta(2)

urlpatterns = [
    path("classes/", classes_view(MagicMock()), name="create_classes")
]


@pytest.fixture
def mock_yoga_class() -> YogaClass:
    return YogaClass(
        id=test_class_id,
        start_time=test_future_date,
        class_name="vinyasa",
        class_level="intermediate",
        max_capacity=10,
        current_capacity=10,
        location="home",
    )


@pytest.fixture
def yoga_class_response():
    return {
        "id": f"{test_class_id}",
        "start_time": test_future_date.isoformat(),
        "class_name": "vinyasa",
        "class_level": "intermediate",
        "max_capacity": 10,
        "current_capacity": 10,
    }


# ------------- Test POST api/v1/classes ---------------
@patch("yoga_app.classes.interfaces.api.views.ClassesService")
@pytest.mark.django_db
def test_create_classes_success(mock_service, mock_yoga_class, yoga_class_response):
    mock_service.return_value.create_classes.return_value = [mock_yoga_class]

    client = Client()
    body = [
        {
            "start_time": "2025-09-20T10:00:00Z",
            "class_level": "intermediate",
            "class_name": "vinyasa",
            "max_capacity": 10,
            "location": "home"
        }
    ]

    response = client.post("/", data=body, content_type="application/json")

    assert response.status_code == 200
    data = response.json()
    assert data["classes"][0] == yoga_class_response

