import names

from api.work_package_api import WorkPackageApi
from open_project_config import api_config


def test_create_new_work_package():
    expected_work_package_subject = names.get_full_name()

    payload = {"subject": expected_work_package_subject, "type": {"href": "/api/v3/types/1", "title": "Task"},
               "project": {"href": "/api/v3/projects/102", "title": "TestProject1"},
               "status": {"href": "/api/v3/statuses/1", "title": "New"}}

    work_package_api = WorkPackageApi(api_config["base_url"])
    work_package_response = work_package_api.create_work_package(payload)
    assert expected_work_package_subject == work_package_response.json()["subject"], f"The subject should be {expected_work_package_subject}"
