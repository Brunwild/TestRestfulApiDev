import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        'name': 'MSI Katana',
        'data': {
            'year': 2023,
            'price': 1495.95,
            'CPU model': 'Intel Core i7',
            'Graphics card': 'GeForce RTX 4070'
        }
    }

    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])