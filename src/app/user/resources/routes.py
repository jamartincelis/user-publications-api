from .user import UserList, UserDetail, UserLoginAuth

def initialize_user_routes(api):
    api.add_resource(UserList, '/api/users')
    api.add_resource(UserDetail, '/api/users/<int:id>')
    api.add_resource(UserLoginAuth, '/api/users/login')