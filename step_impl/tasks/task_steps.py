import requests
import json

from getgauge.python import step, data_store

BASE_URL = "http://127.0.0.1:8000"  # адрес FastAPI


# -------------------------
# Проверка доступности API
# -------------------------
@step("the API is running")
def api_is_running():
    response = requests.get(f"{BASE_URL}/docs")
    assert response.status_code == 200, f"API is not running, status: {response.status_code}"


# -------------------------
# POST /tasks
# -------------------------
@step("I send a POST request to <endpoint> with payload <payload>")
def send_post_request(endpoint, payload):
    data = json.loads(payload)
    response = requests.post(f"{BASE_URL}{endpoint}", json=data)
    data_store.suite["response"] = response


# -------------------------
# GET /tasks/{id}
# -------------------------
@step("I send a GET request for task with id <task_id_key>")
def send_get_request(task_id_key):
    if task_id_key not in data_store.suite:
        raise KeyError(f"Key '{task_id_key}' not found in data_store")

    task_id = data_store.suite[task_id_key]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    data_store.suite["response"] = response


@step("I send a GET request to <url>")
def send_get_request_to_url(url):
    """Для негативных тестов с несуществующими ID"""
    response = requests.get(f"{BASE_URL}{url}")
    data_store.suite["response"] = response


# -------------------------
# GET /tasks
# -------------------------
@step("I send a GET request to </tasks> for get all tasks")
def send_get_request(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    data_store.suite["response"] = response


# -------------------------
# PUT /tasks/{id}
# -------------------------
@step("I send a PUT request for task with id <task_id_key> with payload <payload>")
def send_put_request_by_id(task_id_key, payload):
    if task_id_key not in data_store.suite:
        raise KeyError(f"Key '{task_id_key}' not found in data_store")

    task_id = data_store.suite[task_id_key]
    data = json.loads(payload)
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=data)
    data_store.suite["response"] = response


@step("I send a PUT request to <url> with payload <payload>")
def send_get_request_to_url(url, payload):
    """Для негативных тестов с несуществующими ID"""
    data = json.loads(payload)
    response = requests.put(f"{BASE_URL}{url}", json=data)
    data_store.suite["response"] = response


# -------------------------
# DELETE /tasks/{id}
# -------------------------
@step("I send a DELETE request for task with id <task_id_key>")
def send_delete_request_by_id(task_id_key):
    if task_id_key not in data_store.suite:
        raise KeyError(f"Key '{task_id_key}' not found in data_store")

    task_id = data_store.suite[task_id_key]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    data_store.suite["response"] = response


@step("I send a DELETE request to <url>")
def send_get_request_to_url(url):
    """Для негативных тестов с несуществующими ID"""
    response = requests.delete(f"{BASE_URL}{url}")
    data_store.suite["response"] = response


# -------------------------
# Проверка кода ответа
# -------------------------
@step("the response status code should be <status_code>")
def check_status_code(status_code):
    response = data_store.suite["response"]
    expected_code = int(status_code)
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"


# -------------------------
# Проверка тела ответа
# -------------------------
@step("the response should contain <payload>")
def check_response(payload):
    data = json.loads(payload)
    actual = data_store.suite["response"].json()

    for key, value in data.items():
        assert str(actual[key]) == value, f"For key '{key}', expected '{value}', got '{actual[key]}'"


# -------------------------
# Проверка непустого массива
# -------------------------
@step("the response should be a non-empty array")
def check_non_empty_array():
    response = data_store.suite["response"]
    actual = response.json()
    assert isinstance(actual, list), f"Expected array, got {type(actual)}"
    assert len(actual) > 0, "Expected non-empty array"


# -------------------------
# Проверка наличия задачи в списке
# -------------------------
@step("the response should contain task with id <task_id_key>")
def check_task_in_list(task_id_key):
    task_id = data_store.suite[task_id_key]
    response = data_store.suite["response"]
    tasks = response.json()

    task_found = any(task["id"] == task_id for task in tasks)
    assert task_found, f"Task with ID {task_id} not found in the list"


# -------------------------
# Сохранение ID созданной задачи
# -------------------------
@step("save the response task id as <key>")
def save_task_id(key):
    response = data_store.suite["response"]
    task_data = response.json()
    data_store.suite[key] = task_data["id"]


# -------------------------
# Проверка удаления задачи
# -------------------------
@step("verify task <task_id_key> is deleted")
def verify_task_deleted(task_id_key):
    task_id = data_store.suite[task_id_key]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")

    if response.status_code != 404:
        # Если API возвращает 200, проверяем, что задачи нет в списке
        all_tasks_response = requests.get(f"{BASE_URL}/tasks")
        all_tasks = all_tasks_response.json()

        task_still_exists = any(str(task["id"]) == str(task_id) for task in all_tasks)
        assert not task_still_exists, f"Task with ID {task_id} still exists after deletion"
