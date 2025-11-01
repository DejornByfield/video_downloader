from flask import Flask
from .database import db
from .routes import main
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Ensure the download folder exists
    os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

    # Register routes 
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app