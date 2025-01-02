from . import chatbot
from .chatbot import api, browser, advanced_chatbot,chatbot_base, chatbot, speech_handler

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprint
    from .routes import main
    app.register_blueprint(main)
    
    return app
