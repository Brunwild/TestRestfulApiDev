from endpoints.object import ObjectEndpoints

class ObjectAsserts(ObjectEndpoints):
    def check_response_name(self, name, response_json):
        assert response_json['name'] == name, f"Ожидалось имя {name}, получено {response_json['name']}"

    def check_response_id(self, object_id, response_json):
        assert response_json['id'] == object_id, f"Ожидался ID {object_id}, получен {response_json['id']}"
