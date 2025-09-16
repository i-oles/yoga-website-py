import datetime
import uuid
import pytest
from datetime import timedelta
from unittest.mock import MagicMock
from django.test import Client
from django.urls import path
from yoga_app.apps.classes.domain.entities import YogaClass
from yoga_app.apps.classes.interfaces.api.views import classes_view

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
        "start_time": f"{test_future_date}",
        "class_name": "vinyasa",
        "class_level": "intermediate",
        "max_capacity": 10,
        "current_capacity": 10,
    }


# ------------- Test POST api/v1/classes ---------------
@pytest.mark.django
def test_create_classes_success(mock_yoga_class, yoga_class_response):
    mock_service = MagicMock()
    mock_service.create_classess.return_value = [mock_yoga_class]

    _ = classes_view(mock_service)

    client = Client()

    body = [
        {
            "start_time": f"{test_future_date}",
            "class_level": "intermediate",
            "class_name": "vinyasa",
            "max_capacity": 10,
            "location": "home"
        }
    ]

    response = client.post("/classes/", data=body, content_type="application/json")
    assert response.status_code == 200
    data = response.body
    assert "classes" in data
    assert data["classes"][0] == yoga_class_response
