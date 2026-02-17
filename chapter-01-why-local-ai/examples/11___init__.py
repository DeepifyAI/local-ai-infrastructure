#!/usr/bin/env python3
# local_ai_hello_world.py
"""
Complete local AI starter - demonstrates best practices.
"""

from ollama import chat
import json
import time
from typing import List, Dict

class LocalAI:
    """Simple wrapper for local Ollama inference."""
    
    def __init__(self, model: str = 'gemma2:2b', timeout: int = 30):
        self.model = model
        self.timeout = timeout
        self.conversation_history: List[Dict] = []
    
    def chat(self, message: str, stream: bool = False) -> str:
        """Send a message and get response."""
        
        # Add to history
        self.conversation_history.append({
            'role': 'user',
            'content': message
        })
        
        start_time = time.time()
        
        try:
            response = chat(
                model=self.model,
                messages=self.conversation_history,
                stream=stream
            )
            
            reply = response['message']['content']
            latency = (time.time() - start_time) * 1000
            
            # Add to history
            self.conversation_history.append({
                'role': 'assistant',
                'content': reply
            })
            
            print(f"[Latency: {latency:.0f}ms]")
            return reply
            
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def clear_history(self):
        """Reset conversation."""
        self.conversation_history = []
    
    def save_history(self, filename: str):
        """Save conversation to file."""
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
        print(f"Saved conversation to {filename}")
    
    def load_history(self, filename: str):
        """Load conversation from file."""
        with open(filename, 'r') as f:
            self.conversation_history = json.load(f)
        print(f"Loaded conversation from {filename}")

# Example usage
if __name__ == '__main__':
    ai = LocalAI(model='gemma2:2b')
    
    print("Local AI Chat (type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            # Save on exit
            ai.save_history('conversation.json')
            break
        
        response = ai.chat(user_input)
        print(f"AI: {response}\n")
