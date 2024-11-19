import pytest
import allure

from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

@allure.feature('Create object')
def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
        'name': 'MSI Katana',
        'data': {
            'year': 2023,
            'price': 1495.95,
            'CPU model': 'Intel Core i7',
            'Graphics card': 'GeForce RTX 4070'
        }
    }
    with allure.step('Создется объект'):
        new_object_endpoint.new_object(payload=payload)
    with allure.step('Проверка статус кода'):
        new_object_endpoint.check_response_is_200()
    with allure.step('Проверка совпаденеия графы "name"'):
        new_object_endpoint.check_name(payload['name'])

@allure.feature('Get object by id')
def test_get_object(obj_id):
    with allure.step('Обращаемся к объекту по id'):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_by_id(obj_id)
    with allure.step('Проверка статус кода'):
        get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)
    #get_obj_endpoint.check_response_is_404() Вариант негативного теста

@allure.feature('Update object')
def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    payload = {
        'name': 'MSI Katana 2',
        'data': {
            'year': 2024,
            'price': 1889.95,
            'CPU model': 'Intel Core i7',
            'Graphics card': 'GeForce RTX 4090'
        }
    }
    with allure.step('Обновляем данные объекта'):
        update_obj_endpoint.update_by_id(obj_id, payload)
    with allure.step('Проверка статус кода'):
        update_obj_endpoint.check_response_is_200()
    with allure.step('Проверка совпаденеия графы "name"'):
        update_obj_endpoint.check_response_name(payload['name'])

@allure.feature('Delete object')
def test_delete_object(obj_id):
    with allure.step('Удаляем объект'):    
        delete_obj_endpoint = DeleteObject()
        delete_obj_endpoint.delete_by_id(obj_id)
    with allure.step('Проверка статус кода'):
        delete_obj_endpoint.check_response_is_200()
    with allure.step('Обращаемся к объекту по id'):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_by_id(obj_id)
    with allure.step('Проверка статус кода'):
        get_obj_endpoint.check_response_is_404()