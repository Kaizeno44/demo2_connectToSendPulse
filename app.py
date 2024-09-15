import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lấy API key từ biến môi trường
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )

    gpt_reply = response.choices[0].text.strip()

    return jsonify({
        'reply': gpt_reply
    })

@app.route('/')
def home():
    return 'Hello, Flask is running on Railway!'

if __name__ == '__main__':
    app.run(debug=True)
