import pytest
from rest_framework.test import APIClient
from tasks.models import Task
from django.db import models


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    payload = {
        "title": "Test py django",
        "description": "This is a test task",
        "completed": False,
    }
    response = client.post("/api/tasks/", payload, format="json")

    assert response.status_code == 201
    assert Task.objects.count() == 1
    task = Task.objects.first()
    assert task.title == payload["title"]


@pytest.mark.django_db
def test_list_tasks():
    Task.objects.create(
        title="Task 1", description="This is a test task", completed=False
    )
    Task.objects.create(
        title="Task 2", description="This is a test task", completed=True
    )

    client = APIClient()
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_update_task():
    task = Task.objects.create(title="Original", description="desc", completed=False)

    client = APIClient()
    payload = {"title": "Changed", "description": "desc", "completed": True}
    response = client.put(f"/api/tasks/{task.id}/", payload, format="json")

    assert response.status_code == 200
    updated_task = Task.objects.get(id=task.id)
    assert updated_task.title == "Changed"
    assert updated_task.completed is True


@pytest.mark.django_db
def test_delete_task():
    task = Task.objects.create(title="Delete", description="", completed=False)

    client = APIClient()
    response = client.delete(f"/api/tasks/{task.id}/")
    assert response.status_code == 204
    assert Task.objects.count() == 0


@pytest.mark.django_db
def test_task_not_found():
    max_id = Task.objects.aggregate(max_id=models.Max("id"))["max_id"] or 0
    non_existent_id = max_id + 1

    client = APIClient()
    response = client.get(f"/api/tasks/{non_existent_id}/")
    assert response.status_code == 404
