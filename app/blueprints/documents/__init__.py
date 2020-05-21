from flask import Blueprint

bp = Blueprint(name = 'documents', 
    import_name = __name__, 
    template_folder = 'templates')

from app.blueprints.documents import api