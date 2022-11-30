""" import pytest
import json
from http_async_client.persons_service import getPersons

def get_a_created_person():
    firstPerson = '{"id": 1,"name": "Isa","age": 18}'
    personJson = json.loads(firstPerson)
    response = getPersons()
    assert response[0] == personJson """