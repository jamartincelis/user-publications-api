from .publication import PublicationDetail, PublicationList

def initialize_publication_routes(api):
    api.add_resource(PublicationList, '/api/users/<int:user_id>/publications')
    api.add_resource(PublicationDetail, '/api/users/<int:user_id>/publications/<int:publication_id>')