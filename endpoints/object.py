import requests

URL = 'https://api.restful-api.dev'

class ObjectEndpoints:
    def __init__(self):
        self.response = None
        self.response_json = None

    def _handle_response(self):
        """Обрабатывает ответ"""
        self.response_json = self.response.json()
        return self.response_json

    def new_object(self, payload):
        self.response = requests.post(f'{URL}/objects', json=payload)
        return self._handle_response()

    def get_by_id(self, object_id):
        self.response = requests.get(f'{URL}/objects/{object_id}')
        return self._handle_response()

    def update_by_id(self, object_id, payload):
        self.response = requests.put(f'{URL}/objects/{object_id}', json=payload)
        return self._handle_response()

    def delete_by_id(self, object_id):
        self.response = requests.delete(f'{URL}/objects/{object_id}')
        return self._handle_response()