from api.api_rest import ApiRequests


class WorkPackageApi(ApiRequests):
    def __init__(self, base_url):
        base_url_work_package = base_url + "/api/v3/work_packages/"
        super(WorkPackageApi, self).__init__(base_url_work_package)

    def get_work_package_by_id(self, get_id):
        add_url = self.base_url + str(get_id)
        return self.my_get(add_url)

    def update_work_package_by_id(self, update_id, paylode):
        add_url = self.base_url + str(update_id)
        return self.my_patch(add_url, payload=paylode)

    def create_work_package(self, paylode):
        return self.my_post(self.base_url, payload=paylode)

    def delete_work_package(self, delete_id):
        add_url = self.base_url + str(delete_id)
        return self.my_delete(add_url)
