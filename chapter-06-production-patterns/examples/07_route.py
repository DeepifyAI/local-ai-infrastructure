#!/usr/bin/env python3
class RouterAgent:
    def route(self, query):
        prompt = f"What type of question is this: technical, creative, or factual? Query: {query}"
        response = ollama.generate(model='gemma2:2b', prompt=prompt)
        return response['response'].lower()

class TechnicalAgent:
    def answer(self, query):
        return ollama.chat(model='llama3.1:8b', messages=[
            {'role': 'system', 'content': 'You are a technical expert.'},
            {'role': 'user', 'content': query}
        ])['message']['content']

class CreativeAgent:
    def answer(self, query):
        return ollama.chat(model='llama3.1:8b', messages=[
            {'role': 'system', 'content': 'You are a creative writer.'},
            {'role': 'user', 'content': query}
        ])['message']['content']

# Usage
router = RouterAgent()
tech = TechnicalAgent()
creative = CreativeAgent()

query = "Write a poem about Python"
task_type = router.route(query)

if 'creative' in task_type:
    print(creative.answer(query))
elif 'technical' in task_type:
    print(tech.answer(query))
