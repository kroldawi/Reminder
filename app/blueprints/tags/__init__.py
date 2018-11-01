from flask import Blueprint

bp = Blueprint(name = 'tags', 
    import_name = __name__, 
    template_folder = 'templates')

from app.blueprints.tags import api