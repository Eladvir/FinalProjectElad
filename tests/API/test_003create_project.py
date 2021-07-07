import names

from api.project_api import ProjectApi
from open_project_config import api_config


def test_create_new_project():
    project_name = names.get_first_name()
    expected_project_identifier = names.get_last_name().lower()

    payload = {"name": project_name, "identifier": expected_project_identifier,
               "_links": {"scope": {"href": f'/projects/{project_name}'}}}
    projects_api = ProjectApi(api_config["base_url"])
    project_response = projects_api.creat_project(payload)

    assert project_name == project_response.json()["name"], f"The project name should be {project_name}"
    assert expected_project_identifier == project_response.json()["identifier"], f"The description should be {expected_project_identifier}"
