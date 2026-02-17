#!/usr/bin/env python3
from flask import Flask, request, Response, stream_with_context
import ollama

app = Flask(__name__)

@app.route('/stream', methods=['POST'])
def stream():
    data = request.json
    prompt = data['prompt']
    
    def generate():
        for chunk in ollama.generate(model='llama3.1:8b', prompt=prompt, stream=True):
            yield f"data: {chunk['response']}\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run()
