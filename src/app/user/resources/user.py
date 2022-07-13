from flask import jsonify, request
from flask_restful import Resource
from ..models import User
from flask_jwt_extended import create_access_token
from app import jwt


class UserList(Resource):
    """
    Permite listar o crear usuarios.
    """
    def get(self):
        users = User.query.all()
        return jsonify([user.to_json() for user in users])

    def post(self):
        try:
            body = request.get_json()
            user =  User(**body)
            db.session.add(user)
            db.session.commit()

            user_id = user.id
            return {'id': str(user_id)}, 200
        except Exception as e:
            return {'error': f'No se pudo crear el usuario {e}'}, 500


class UserDetail(Resource):
    """
    Permite actualizar o eliminar usuarios.
    """       
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            return {'error': "User {} doesn't exist".format(id)}, 404
        return jsonify(user.to_json())

    def put(self, id):
        try:
            if not request.json:
                return {'error': "Bad request"}, 400
            user = User.query.get(id)
            if user is None:
                return {'error': "User {} doesn't exist".format(id)}, 404

            user.full_name = request.json.get('full_name', user.full_name)
            user.email = request.json.get('email', user.email)
            user.status = request.json.get('status', user.status)
            db.session.commit()
            return jsonify(user.to_json())
        except Exception as e:
            return {'error': f'No se pudo actualizar el usuario {e}'}, 500


    def delete(self, id):
        user = User.query.get(id)
        if user is None:
             return {'error': "User {} doesn't exist".format(id)}, 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'result': True})        

class UserLoginAuth(Resource):
    """
    Permite autenticar usuarios.
    """
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

"""class UserLogout(Resource):
    
    #Permite desloguear al usuario.
           
    def delete(self, id):
        token = get_jwt()
        jti = token["jti"]
        ttype = token["type"]
        now = datetime.now(timezone.utc)
        db.session.add(TokenBlocklist(jti=jti, type=ttype, created_at=now))
        db.session.commit()
        return jsonify(msg=f"{ttype.capitalize()} token successfully revoked")""" 