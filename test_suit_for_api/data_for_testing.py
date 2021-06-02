import requests
import configparser

class UserClient:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    URL = parser.get('URL', 'SERVICE_URL')

    def __get_user(self, username = None, department = None):
        if username == None and department == None:
            r = requests.get(UserClient.URL)
        elif username != None and department != None:
            r = requests.get(UserClient.URL + '?username=' + username + '&department=' + department)
        elif department == None:
            r = requests.get(UserClient.URL + '?username=' + username)
        elif username == None:
            r = requests.get(UserClient.URL + '?department=' + department)
        return r.text