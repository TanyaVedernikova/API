import requests
import configparser
import json
import random

class UserClient:

    def get_user(self, username = None, department = None):
        def __get_user():
            parser = configparser.ConfigParser()
            parser.read('config.ini')
            URL = parser.get('URL', 'SERVICE_URL')
            params = {'username' : username, 'department' : department}
            response = requests.get(URL + "users", params)
            return response
        return __get_user()



