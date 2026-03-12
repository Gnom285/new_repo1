
import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")


@pytest.fixture
def auth_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def project_id(auth_headers):
    payload = {"title": "Temporary Test Project"}
    response = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=auth_headers
    )
    data = response.json()
    p_id = data.get("id")
    yield p_id


def test_create_project_positive(auth_headers):
    payload = {"title": "New Pytest Project"}
    response = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=auth_headers
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title(auth_headers):
    payload = {"title": ""}
    response = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=auth_headers
    )
    assert response.status_code == 400


def test_get_project_positive(auth_headers, project_id):
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_invalid_id(auth_headers):
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(
        f"{BASE_URL}/projects/{invalid_id}",
        headers=auth_headers
    )
    assert response.status_code == 404


def test_update_project_positive(auth_headers, project_id):
    new_title = "Updated Project Title"
    payload = {"title": new_title}
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json=payload,
        headers=auth_headers
    )
    assert response.status_code == 200


def test_update_project_negative_no_auth(project_id):
    payload = {"title": "No Auth Title"}
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code in [401, 403]
