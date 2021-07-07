import requests

from open_project_config import api_config

username = api_config["username"]
password = api_config["password"]


class ApiRequests:

    def __init__(self, base_url):
        self.base_url = base_url
        self.auth = (api_config["username"], api_config["password"])

    def my_get(self, get_url_path):
        return requests.get(get_url_path, auth=self.auth)

    def my_post(self, post_url_path, payload):
        return requests.post(post_url_path, json=payload, auth=self.auth)

    def my_patch(self, patch_url_path, payload):
        return requests.patch(patch_url_path, json=payload, auth=self.auth)

    def my_delete(self, delete_url_path):
        return requests.delete(delete_url_path, auth=self.auth, json={})
