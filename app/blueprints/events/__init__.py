from flask import Blueprint

bp = Blueprint(name = 'events', 
    import_name = __name__, 
    template_folder = 'templates')

from app.blueprints.events import api