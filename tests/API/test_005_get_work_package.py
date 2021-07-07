from api.work_package_api import WorkPackageApi
from open_project_config import api_config


def test_get_work_package_by_id():
    work_packages_api = WorkPackageApi(api_config["base_url"])
    expected_work_package_type = "Task"
    expected_work_package_subject = "My Task 1"
    package_id = "214"
    expected_status_code = 200

    work_package_response = work_packages_api.get_work_package_by_id(package_id)

    assert work_package_response.status_code == expected_status_code, f"The status code should be {expected_status_code}"
    assert work_package_response.json()["subject"] == expected_work_package_subject, f"The subject should be {expected_work_package_subject}"
    assert work_package_response.json()["_embedded"]["type"]["name"] == expected_work_package_type, f"The name should be {expected_work_package_type}"
