from api.project_api import ProjectApi
from open_project_config import api_config


def test_get_project_by_id():
    projects_api = ProjectApi(api_config["base_url"])
    project_id = "806"
    expected_project_name = "Elad-TestProject1"
    expected_project_description = "This is the first test project"
    expected_status_code = 200

    project_response = projects_api.get_project_by_id(project_id)

    assert project_response.json()["name"] == expected_project_name, f"The name should be {expected_project_name}"
    assert project_response.status_code == expected_status_code, f"The status should be {expected_status_code}"
    assert project_response.json()["description"]["raw"] == expected_project_description, f"The id should be {expected_project_description}"
