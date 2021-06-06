import cherrypy
import json

@cherrypy.tools.json_out()
@cherrypy.expose
class Users:

    path = 'data_users.json'
    with open(path, 'r') as f:
        data_users = json.loads(f.read())

    def GET(self, username=None, department=None):
        if username == None:
            data1 = Users.data_users["users"]
        else:
            data1 = [user for user in Users.data_users["users"] if user["username"].find(username) != -1]
        if department == None:
            data2 = Users.data_users["users"]
        else:
            data2 = [user for user in Users.data_users["users"] if user["department"].find(department) != -1]
        data3 = [user for user in data1 if user in data2]
        return data3

@cherrypy.tools.json_out()
@cherrypy.expose
class Department:

    path = 'data_users.json'
    with open(path, 'r') as f:
        data_users = json.loads(f.read())

    def GET(self, name=None):
        if name == None:
            data1 = [user["department"] for user in Users.data_users["users"]]
        else:
            data1 = [user for user in Users.data_users["users"] if user["department"].find(name_of_department) != -1]
        return data1

def start_api():
    cherrypy.engine.start()
    cherrypy.engine.block()
def finish_api():
    cherrypy.engine.stop()

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
start_api()


