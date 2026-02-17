#!/usr/bin/env python3
from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    model = data.get('model', 'llama3.1:8b')
    
    response = ollama.chat(model=model, messages=messages)
    
    return jsonify({
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': response['message']['content']
            }
        }]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
