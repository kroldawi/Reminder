from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.blueprints.tags import bp as tags_bp
from app.blueprints.things import bp as things_bp
from app.blueprints.events import bp as events_bp

app.register_blueprint(tags_bp, url_prefix='/tags')
app.register_blueprint(things_bp, url_prefix='/things')
app.register_blueprint(events_bp, url_prefix='/events')

from app import routes