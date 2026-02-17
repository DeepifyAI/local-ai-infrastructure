#!/usr/bin/env python3
import ollama

class RouterAgent:
    def route(self, query):
        prompt = f"What type of question is this: technical, creative, or factual? Reply with one word only. Query: {query}"
        response = ollama.generate(model='gemma2:9b', prompt=prompt)
        return response['response'].lower()

class TechnicalAgent:
    def answer(self, query):
        return ollama.chat(model='gemma2:9b', messages=[
            {'role': 'system', 'content': 'You are a concise technical expert. Keep answers under 3 sentences.'},
            {'role': 'user', 'content': query}
        ])['message']['content']

class CreativeAgent:
    def answer(self, query):
        return ollama.chat(model='gemma2:9b', messages=[
            {'role': 'system', 'content': 'You are a creative writer. Write short, punchy responses.'},
            {'role': 'user', 'content': query}
        ])['message']['content']

# Usage
router = RouterAgent()
tech = TechnicalAgent()
creative = CreativeAgent()

query = "Write a short poem about Python"
print(f"Query: {query}")
task_type = router.route(query)
print(f"Routed to: {task_type.strip()}")
print()

if 'creative' in task_type:
    print(creative.answer(query))
elif 'technical' in task_type:
    print(tech.answer(query))
else:
    # Default to creative for ambiguous routing
    print(creative.answer(query))
