import time
import allure
import names
from api.work_package_api import WorkPackageApi
from open_project_config import api_config


@allure.description("delete  the project")
def test_delete_work_package_id():
    # creating project
    expected_status_code_creating = 201
    work_package_name = names.get_first_name()

    payload = {"subject": work_package_name, "type": {"href": "/api/v3/types/1", "title": "Task"},
               "project": {"href": "/api/v3/projects/102", "title": "TestProject1"},
               "status": {"href": "/api/v3/statuses/1", "title": "New"}}

    work_package_api = WorkPackageApi(api_config["base_url"])
    work_package_response = work_package_api.create_work_package(payload)
    assert expected_status_code_creating == work_package_response.status_code,f"The status code after creating work package should be {expected_status_code_creating}"
    id_project_to_delete = work_package_response.json()["id"]

    # delete project
    expected_status_code_deleting = 204
    time.sleep(10)
    work_package_response = work_package_api.delete_work_package(id_project_to_delete)
    assert work_package_response.status_code == expected_status_code_deleting,f"The status code after deleting work package should be {expected_status_code_deleting}"
    time.sleep(5)

    # getting project after delete
    expected_status_code_getting = 404
    work_package_response = work_package_api.get_work_package_by_id(id_project_to_delete)
    assert work_package_response.status_code == expected_status_code_getting,f"The status code after getting work package should be {expected_status_code_getting}"
