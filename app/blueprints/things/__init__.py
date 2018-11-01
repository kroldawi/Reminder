from flask import Blueprint

bp = Blueprint(name = 'things', 
    import_name = __name__, 
    template_folder = 'templates')

from app.blueprints.things import api