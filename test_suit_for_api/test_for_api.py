import pytest
import logging
import datetime
from client import UserClient

name_log = str(datetime.datetime.now())
name_log = name_log.replace(' ', '_')
name_log = name_log.replace('.', '_')
name_log = name_log.replace(':', '_')
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG, filename=name_log + '.log')

open(str(name_log + '.log'), "w+")


def test_check_availability_users_status_200(user):
    user.get_user().raise_for_status()
    logging.info("users answer 200")

def test_username(random_user_data, user):
    res = user.get_user(username=random_user_data["username"])
    assert res.json().pop() == random_user_data



def test_department(random_user_data, user):
    res = user.get_user(department=random_user_data["department"])
    assert res.json().pop() == random_user_data

def test_username_and_department(random_user_data, user):
    res = user.get_user(username=random_user_data["username"],department=random_user_data["department"])
    assert res.json().pop() == random_user_data






