import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):
    
    def get_by_id(self, object_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id

    def check_response_is_404(self):
        assert self.response.status_code == 404