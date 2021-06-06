import pytest
import datetime
import logging
import json
import random
from client import UserClient

@pytest.fixture
def user():
    new_test_object = UserClient()
    return new_test_object

@pytest.fixture
def random_user_data():
    path = 'data_users.json'
    with open(path, 'r') as f:
        data_users = json.loads(f.read())
    data_user = random.choice(data_users["users"])
    return data_user

