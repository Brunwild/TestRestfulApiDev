import pytest
import allure

from assertions.positive_object_assert import ObjectAsserts
from endpoints.object import ObjectEndpoints
from conftest import payload_create, pyload_update

@allure.feature('When create object')
def test_create_object():
    new_object_endpoint = ObjectEndpoints()
    payload = payload_create
    
    with allure.step('Then create object'):
        response_json = new_object_endpoint.new_object(payload=payload)
    obj_asserts = ObjectAsserts()
    with allure.step('Then if the request is ok, code 200 will be responced'):
        assert new_object_endpoint.response.status_code == 200
    with allure.step('Then expected id matches the one you get'):
        obj_asserts.check_response_id(response_json['id'], response_json)
    with allure.step('Then expected name matches the one you get'):
        obj_asserts.check_response_name(payload['name'], response_json)

@allure.feature('When getting an object by id')
def test_get_object(obj_id):
    get_obj_endpoint = ObjectEndpoints()
    with allure.step('Then getting an object by id'):
        response_json = get_obj_endpoint.get_by_id(obj_id)
    with allure.step('Then if the request is ok, code 200 will be responced'):
        assert get_obj_endpoint.response.status_code == 200
    expected_header_value = 'application/json'
    with allure.step('Then check the response header'):
        assert get_obj_endpoint.response.headers['Content-Type'] == expected_header_value, \
            f"Ожидался заголовок 'Content-Type' со значением '{expected_header_value}', но получено '{get_obj_endpoint.response.headers['Content-Type']}'"
    obj_asserts = ObjectAsserts()
    with allure.step('Then expected id matches the one you get'):
        obj_asserts.check_response_id(obj_id, response_json)

@allure.feature('When update object')
def test_update_object(obj_id):
    update_obj_endpoint = ObjectEndpoints()
    payload = pyload_update
    with allure.step('Then updating object'):
        response_json = update_obj_endpoint.update_by_id(obj_id, payload)
    obj_asserts = ObjectAsserts()
    with allure.step('Then if the request is ok, code 200 will be responced'):
        assert update_obj_endpoint.response.status_code == 200
    with allure.step('Then expected id matches the one you get'):
        obj_asserts.check_response_id(obj_id, response_json)
    with allure.step('Then expected name matches the one you get'):
        obj_asserts.check_response_name(payload['name'], response_json)

@allure.feature('When delete object')
def test_delete_object(obj_id):
    delete_obj_endpoint = ObjectEndpoints()
    with allure.step('Then delete object by id'):    
        delete_obj_endpoint.delete_by_id(obj_id)
    with allure.step('Then if the request is ok, code 200 will be responced'):
        assert delete_obj_endpoint.response.status_code == 200
    with allure.step('Then try get object'):
        get_obj_endpoint = ObjectEndpoints()
        get_obj_endpoint.get_by_id(obj_id)
    with allure.step('Then if the object is deleted, code 404 will be responced'):
        assert get_obj_endpoint.response.status_code == 404