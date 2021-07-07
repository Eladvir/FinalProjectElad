from api.api_rest import ApiRequests


class ProjectApi(ApiRequests):
    def __init__(self, base_url):
        base_url_project = base_url + "/api/v3/projects/"
        super(ProjectApi, self).__init__(base_url_project)

    def get_project_by_id(self, get_id):
        add_url = self.base_url + str(get_id)
        return self.my_get(add_url)

    def update_project_by_id(self, update_id, paylode):
        add_url = self.base_url + str(update_id)
        return self.my_patch(add_url, payload=paylode)

    def creat_project(self, paylode):
        return self.my_post(self.base_url, payload=paylode)

    def delete_project(self, delete_id):
        delete_url = self.base_url + str(delete_id)
        return self.my_delete(delete_url)
