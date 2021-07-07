from api.project_api import ProjectApi
from open_project_config import api_config


def test_update_project_by_id():
    projects_api = ProjectApi(api_config["base_url"])
    project_id = "105"
    expected_project_description = "this is the $$ new description"

    payload = {"description": {"raw": expected_project_description}}
    project_response = projects_api.update_project_by_id(project_id, payload)

    assert project_response.json()["description"]["raw"] == expected_project_description, f"The description should be {expected_project_description}"
