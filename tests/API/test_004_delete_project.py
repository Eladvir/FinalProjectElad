import time
import allure
import names
from api.project_api import ProjectApi
from open_project_config import api_config


@allure.description("delete  the project")
def test_delete_project_id():
    # creating project
    expected_status_code_creating = 201
    project_name = names.get_first_name()
    payload = {"name": project_name, "_links": {"scope": {"href": f'/projects/{project_name}'}}}
    projects_api = ProjectApi(api_config["base_url"])
    project_response = projects_api.creat_project(payload)
    assert project_response.status_code == expected_status_code_creating, f"The status code after creating project should be {expected_status_code_creating}"
    id_project_to_delete = project_response.json()["id"]

    # deleting project
    expected_status_code_deleting = 204
    time.sleep(10)
    project_response = projects_api.delete_project(id_project_to_delete)
    assert project_response.status_code == expected_status_code_deleting, f"The status code after deleting project should be {expected_status_code_deleting}"
    time.sleep(5)

    # getting project after delete
    expected_status_code_getting = 404
    project_response = projects_api.get_project_by_id(id_project_to_delete)
    assert project_response.status_code == expected_status_code_getting, f"The status code after getting project should be {expected_status_code_getting}"
