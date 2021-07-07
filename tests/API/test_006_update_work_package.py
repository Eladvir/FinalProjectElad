from api.work_package_api import WorkPackageApi
from open_project_config import api_config


def test_update_work_package_by_id():
    work_packages_api = WorkPackageApi(api_config["base_url"])
    package_id = "214"

    # get current lockVersion
    work_package_response = work_packages_api.get_work_package_by_id(package_id)
    current_lockVersion = str(work_package_response.json()["lockVersion"])

    # description update
    work_package_api = WorkPackageApi(api_config["base_url"])
    expected_work_package_description = "this is the new description for today"
    payload = {"description": {"raw": expected_work_package_description}, "lockVersion": current_lockVersion}
    project_response = work_package_api.update_work_package_by_id(package_id, payload)

    assert project_response.json()["description"]["raw"] == expected_work_package_description,f"The description should be {expected_work_package_description}"
