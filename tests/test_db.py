import pytest
import allure
from conftest_db import connect_db, fetch_superhero_names

@allure.feature('When to see if you get the names of superheroes')
def test_fetch_superhero_names(fetch_superhero_names):
    with allure.step('Then that the result is a list'):
        assert isinstance(fetch_superhero_names, list)

@allure.feature('When check for the valide superhero names')
def test_fetch_superhero_names_contains(fetch_superhero_names):
    with allure.step('Then send the valid names'):
        expected_names = [
            'Conan (Earth-616)', 'Natalia Romanova (Earth-616)', 'Captain America (Steven Rogers)'
            ]
        for name in expected_names:
            with allure.step('Then check the valid names'):
                assert name in fetch_superhero_names, f"{name} не найден в списке супергероев."

@allure.feature('When to check the format of superhero names')
def test_superhero_names_format(fetch_superhero_names):   
    for name in fetch_superhero_names:
        with allure.step('Then check that name is a string'):
            assert isinstance(name, str), f"Имя '{name}' должно быть строкой."
        with allure.step('Then check that name must not be empty'):    
            assert len(name) > 0, "Имя супергероя не должно быть пустым."

