from flask import Flask
from extensions import db
from auth import auth_bp

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()

    
    db.init_app(app)

    return app
