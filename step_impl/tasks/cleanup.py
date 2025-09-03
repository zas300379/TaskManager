import requests
from getgauge.python import after_suite, after_spec, after_scenario


BASE_URL = "http://127.0.0.1:8000"


def delete_test_tasks():
    """Удаляет все тестовые задачи"""
    try:
        response = requests.get(f"{BASE_URL}/tasks")
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                if "test" in task.get("title", "").lower():
                    requests.delete(f"{BASE_URL}/tasks/{task['id']}")
                    print(f"Deleted test task: {task['title']} (ID: {task['id']})")
    except Exception as e:
        print(f"Cleanup failed: {e}")


# Очистка после всех спецификаций
@after_suite
def cleanup_after_all_tests():
    print("=== Cleaning up after all tests ===")
    delete_test_tasks()
