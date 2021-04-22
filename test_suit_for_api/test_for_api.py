import pytest
import requests

def test_for_users():
    r = requests.get('http:/localhost:8080//users').text
    assert r == '["Bloom", "Stella", "Musa", "Flora", "Techna"]'

def test_for_department():
    r = requests.get('http://127.0.0.1:8080/department').text
    assert r == '["Fire fairy", "Light fairy", "Music fairy", "Nature fairy", "Technology fairy"]'

def test_for_uniq_username():
    r = requests.get('http://127.0.0.1:8080/users?username=lo').text
    assert r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com", "department": "Fire fairy", "date_joined": "2020-09-10"}, {"id": 3, "username": "Flora", "email": "pes_blatnoy@gmail.com", "department": "Nature fairy", "date_joined": "2020-09-13"}]'

def test_for_uniq_username_and_department():
    r = requests.get('http://127.0.0.1:8080/users?username=lo&department=Fire').text
    assert r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com", "department": "Fire fairy", "date_joined": "2020-09-10"}]'