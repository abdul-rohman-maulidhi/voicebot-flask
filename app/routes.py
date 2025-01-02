from flask import Blueprint, render_template, jsonify, request
from .chatbot.advanced_chatbot import AdvancedChatbot

main = Blueprint("main", __name__)

chatbot = AdvancedChatbot()

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/get_response", methods=["POST"])
def get_response():
    data = request.json
    user_input = data.get("message", "")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

@main.route("/listen_and_respond", methods=["POST"])
def listen_and_respond():
    user_input = chatbot.speech_handler.listen()
    response = chatbot.respond(user_input)
    # Simulasi input suara (fungsi mendengar belum diimplementasikan sepenuhnya)
    return jsonify({"user_input": user_input, "response": response})
