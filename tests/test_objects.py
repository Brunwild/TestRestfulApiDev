import pytest
import allure

from assertions.positive_object_assert import ObjectAsserts
from endpoints.object import ObjectEndpoints
from conftest import payload_create, pyload_update

@allure.feature('Test create object')
def test_create_object():
    new_object_endpoint = ObjectEndpoints()
    payload = payload_create
    
    with allure.step('create object'):
        response_json = new_object_endpoint.new_object(payload=payload)
    obj_asserts = ObjectAsserts()
    with allure.step('check id'):
        obj_asserts.check_response_id(response_json['id'], response_json)
    with allure.step('check name'):
        obj_asserts.check_response_name(payload['name'], response_json)

@allure.feature('Test getting an object by id')
def test_get_object(obj_id):
    get_obj_endpoint = ObjectEndpoints()
    with allure.step('getting an object by id'):
        response_json = get_obj_endpoint.get_by_id(obj_id)
    obj_asserts = ObjectAsserts()
    with allure.step('check id'):
        obj_asserts.check_response_id(obj_id, response_json)

@allure.feature('Test update object')
def test_update_object(obj_id):
    update_obj_endpoint = ObjectEndpoints()
    payload = pyload_update
    with allure.step('update object'):
        response_json = update_obj_endpoint.update_by_id(obj_id, payload)
    obj_asserts = ObjectAsserts()
    with allure.step('check id'):
        obj_asserts.check_response_id(obj_id, response_json)
    with allure.step('check name'):
        obj_asserts.check_response_name(payload['name'], response_json)

@allure.feature('Test delete object')
def test_delete_object(obj_id):
    delete_obj_endpoint = ObjectEndpoints()
    with allure.step('delete object by id'):    
        delete_obj_endpoint.delete_by_id(obj_id)
    with allure.step('request status check'):
        assert delete_obj_endpoint.response.status_code == 200
    with allure.step('try get object by id'):
        get_obj_endpoint = ObjectEndpoints()
        get_obj_endpoint.get_by_id(obj_id)
    with allure.step('if the object is deleted, a 404 code will be responced'):
        assert get_obj_endpoint.response.status_code == 404