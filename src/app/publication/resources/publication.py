from flask import jsonify, request
from flask_restful import Resource
from ..models import Publication
from app import db

class PublicationList(Resource):
    """
    Permite listar o crear usuarios.
    """    
    def get(self, user_id):
        publications = Publication.query.filter_by(user=user_id)
        return jsonify([publication.to_json() for publication in publications])

    def post(self, user_id):
        try:
            body = request.get_json()
            publication =  Publication(**body)

            db.session.add(publication)
            db.session.commit()
            return {'id': str(publication.id)}, 200
        except Exception as e:
            return {'error': f'No se pudo crear la publicacion {e}'}, 500


class PublicationDetail(Resource):
    """
    Permite actualizar o eliminar usuarios.
    """       
    def get(self, user_id, publication_id):
        publication = Publication.query.filter_by(id=publication_id, user=user_id).first()

        if publication is None:
            return {'error': "Publication {} doesn't exist".format(publication_id)}, 404
        return jsonify(publication.to_json())

    def put(self, user_id, publication_id):
        try:
            if not request.json:
                return {'error': "Bad request"}, 400
            publication = Publication.query.filter_by(id=publication_id, user=user_id).first()
            if publication is None:
                return {'error': "Publication {} doesn't exist".format(id)}, 404

            publication.title = request.json.get('title', publication.title)
            publication.description = request.json.get('description', publication.description)
            publication.status = request.json.get('status', publication.status)
            publication.priority = request.json.get('priority', publication.priority)

            db.session.commit()
            return jsonify(publication.to_json())
        except Exception as e:
            return {'error': f'No se pudo crear la publicacion {e}'}, 500

    def delete(self, user_id, publication_id):
        publication = Publication.query.filter_by(id=publication_id, user=user_id).first()
        if publication is None:
             return {'error': "Publication {} doesn't exist".format(id)}, 404
        db.session.delete(publication)
        db.session.commit()
        return jsonify({'result': True})