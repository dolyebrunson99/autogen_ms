from flask import Flask, request, jsonify
from junior_bot import init_chat

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "welcome to Autogen server"

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    msg = request.json['message']
    init_chat(msg)
    return jsonify({'message': 'Message received'}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)