from flask import Blueprint

bp = Blueprint(name = 'nalewki', 
    import_name = __name__, 
    template_folder = 'templates')

from app.blueprints.nalewki import api