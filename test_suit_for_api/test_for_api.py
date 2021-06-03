import pytest
import datetime
import logging
from data_for_testing import UserClient

name_log = str(datetime.datetime.now())
name_log = name_log.replace(' ', '_')
name_log = name_log.replace('.', '_')
name_log = name_log.replace(':', '_')
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG, filename=name_log + '.log')
my_file = open(str(name_log + '.log'), "w+")

@pytest.fixture(scope="function", autouse=True)
def create_new_test_object():
    new_test_object = UserClient()
    return new_test_object

def test_for_users(create_new_test_object):

    if r == '["Bloom", "Stella", "Musa", "Flora", "Techna"]':
        logging.info("ok!!!")
    else:
        logging.error("FAIL")

def test_for_department(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(department='Fir')
    if r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com",' \
                ' "department": "Fire fairy", "date_joined": "2020-09-10"}]':
        logging.info("ok")
    else:
        logging.error("bad")

def test_for_uniq_username(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(username='lo')
    if  r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com", "department": "Fire fairy",' \
                ' "date_joined": "2020-09-10"}, {"id": 3, "username": "Flora", "email": "pes_blatnoy@gmail.com",' \
             ' "department": "Nature fairy", "date_joined": "2020-09-13"}]':
        logging.info("ok")
    else:
        logging.error("bad")

def test_for_uniq_username_and_department(create_new_test_object):
    r = create_new_test_object._UserClient__get_user(username='lo', department='Fire')
    if r == '[{"id": 0, "username": "Bloom", "email": "crazyfrog@dot.com",' \
                ' "department": "Fire fairy", "date_joined": "2020-09-10"}]':
        logging.info("ok")
    else:
        logging.info("bad")

