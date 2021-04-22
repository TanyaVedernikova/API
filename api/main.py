import cherrypy

list_of_users = [
    {'id': 0,
    'username': 'Bloom',
    'email': 'crazyfrog@dot.com',
    'department': 'Fire fairy',
    'date_joined': '2020-09-10'
    },
    {'id': 1,
    'username': 'Stella',
    'email': 'deadinside228@mail.ru',
    'department': 'Light fairy',
    'date_joined': '2020-09-11'
    },
    {'id': 2,
    'username': 'Musa',
    'email': 'dillerganjubas@gmail.com',
    'department': 'Music fairy',
    'date_joined': '2020-09-12'
    },
    {'id': 3,
     'username': 'Flora',
     'email': 'pes_blatnoy@gmail.com',
     'department': 'Nature fairy',
     'date_joined': '2020-09-13'
     },
    {'id': 4,
     'username': 'Techna',
     'email': 'polupoker_and_chilipizdric@gmail.com',
     'department': 'Technology fairy',
     'date_joined': '2020-09-14'
     },
]

@cherrypy.tools.json_out()
@cherrypy.expose
class Users:

    def GET(self, username = None, department = None):
        if username == None and department == None:
            list_of_username = []
            for items in list_of_users:
                list_of_username.append(items.get('username'))
            return list_of_username

        elif department != None and username != None:
            list_of_username = []
            for items in list_of_users:
                if items.get('username').find(username) != -1 and items.get('department').find(department) != -1:
                    list_of_username.append(items)
            return list_of_username

        elif username != None:
            list_of_username = []
            for items in list_of_users:
                if items.get('username').find(username) != -1:
                    list_of_username.append(items)
            return list_of_username

        elif department != None:
            list_of_username = []
            for items in list_of_users:
                if items.get('department').find(department) != -1:
                    list_of_username.append(items)
            return list_of_username

@cherrypy.tools.json_out()
@cherrypy.expose
class Department:

    def GET(self, name = None):
        list_of_departments = []
        if name == None:
            for items in list_of_users:
                list_of_departments.append(items.get('department'))
            return list_of_departments
        else:
            for items in list_of_users:
                if items.get('department').find(name) != -1:
                    list_of_departments.append(items.get('department'))
            return list_of_departments




cherrypy.tree.mount(
    Users(), '/users', {
        '/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
),
cherrypy.tree.mount(
    Department(), '/department', {
        '/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)
cherrypy.config.update({'server.socket_host':'0.0.0.0', 'server.socket_port': 8080})

def start_api():
    cherrypy.engine.start()
    cherrypy.engine.block()
def finish_api():
    cherrypy.engine.stop()


start_api()