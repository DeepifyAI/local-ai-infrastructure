#!/usr/bin/env python3
import ollama

class Agent:
    def __init__(self, model='gemma2:9b', system_prompt=''):
        self.model = model
        self.messages = []
        if system_prompt:
            self.messages.append({'role': 'system', 'content': system_prompt})
    
    def chat(self, user_message):
        self.messages.append({'role': 'user', 'content': user_message})
        
        response = ollama.chat(model=self.model, messages=self.messages)
        assistant_message = response['message']['content']
        
        self.messages.append({'role': 'assistant', 'content': assistant_message})
        
        return assistant_message
    
    def reset(self):
        self.messages = []

# Usage
agent = Agent(system_prompt='You are a concise Python tutor. Keep answers to 2 sentences max.')

print("Q: What is a list comprehension?")
print(agent.chat('What is a list comprehension?'))
print("\nQ: Show me a quick example (uses conversation history)")
print(agent.chat('Show me a one-line example'))  # Remembers context
