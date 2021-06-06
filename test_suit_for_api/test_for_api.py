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
    res = user.get_user()
    res.raise_for_status()
    logging.info("users answer 200")

def test_username(random_user_data, user):
    randoms = random_user_data
    res = user.get_user(username=randoms["username"])
    randoms = "[" + str(random_user_data) + ']'
    assert str(res.json()) == randoms



def test_department(random_user_data, user):
    randoms = random_user_data
    res = user.get_user(department=randoms["department"])
    randoms = "[" + str(random_user_data) + ']'
    assert str(res.json()) == randoms

def test_username_and_department(random_user_data, user):
    randoms = random_user_data
    res = user.get_user(username=randoms["username"], department=randoms["department"])
    randoms = "[" + str(random_user_data) + ']'
    assert str(res.json()) == randoms





