from . import chatbot
from .chatbot import voicebot

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprint
    from .routes import main
    app.register_blueprint(main)
    
    return app
