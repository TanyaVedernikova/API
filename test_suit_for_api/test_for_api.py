import pytest
from data_for_testing import UserClient
from log_for_test import LogTest

@pytest.fixture(scope="session")
def start_log():
    log_test = LogTest()
    log_test.create_log_file()

@pytest.fixture(scope="function", autouse=True)
def create_new_test_object():
    new_test_object = UserClient()
    return new_test_object

def test_for_users(create_new_test_object, start_log):
    r = create_new_test_object._UserClient__get_user()
    assert r == '["Bloom", "Stella", "Musa", "Flora", "Techna"]'

def test_for_department(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(department='Fir')
    assert r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com",' \
                ' "department": "Fire fairy", "date_joined": "2020-09-10"}]'

def test_for_uniq_username(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(username='lo')
    assert r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com", "department": "Fire fairy",' \
                ' "date_joined": "2020-09-10"}, {"id": 3, "username": "Flora", "email": "pes_blatnoy@gmail.com", "department": "Nature fairy", "date_joined": "2020-09-13"}]'

def test_for_uniq_username_and_department(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(username='lo', department='Fire')
    assert r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com",' \
                ' "department": "Fire fairy", "date_joined": "2020-09-10"}]', logging.error()