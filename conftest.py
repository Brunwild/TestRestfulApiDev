import pytest
from endpoints.object import ObjectEndpoints

payload_create = {
        'name': 'MSI Katana',
        'data': {
            'year': 2023,
            'price': 1495.95,
            'CPU model': 'Intel Core i7',
            'Graphics card': 'GeForce RTX 4070'
        }
    }

pyload_update = {
        'name': 'MSI Katana 2',
        'data': {
            'year': 2024,
            'price': 1889.95,
            'CPU model': 'Intel Core i7',
            'Graphics card': 'GeForce RTX 4090'
        }
    }

@pytest.fixture()
def obj_id():
    create_object = ObjectEndpoints()
    payload = payload_create
    response_json = create_object.new_object(payload)
    yield response_json['id']
    delete_object = ObjectEndpoints()
    delete_object.delete_by_id(response_json['id'])

