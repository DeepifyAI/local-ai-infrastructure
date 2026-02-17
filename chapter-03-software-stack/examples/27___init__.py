#!/usr/bin/env python3
# ollama_client.py
"""
Production Ollama client with retry logic.
"""

import time
from typing import List, Dict, Optional
from ollama import chat, ChatResponse

class OllamaClient:
    """Robust Ollama client."""
    
    def __init__(
        self,
        model: str,
        host: str = 'http://localhost:11434',
        timeout: int = 60,
        max_retries: int = 3
    ):
        self.model = model
        self.host = host
        self.timeout = timeout
        self.max_retries = max_retries
        self.conversation_history: List[Dict] = []
    
    def chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        stream: bool = False
    ) -> Optional[str]:
        """Send a message and get response."""
        
        # Build messages
        messages = []
        
        if system_prompt:
            messages.append({'role': 'system', 'content': system_prompt})
        
        # Add history
        messages.extend(self.conversation_history)
        
        # Add current message
        messages.append({'role': 'user', 'content': message})
        
        # Try with retries
        for attempt in range(self.max_retries):
            try:
                response = chat(
                    model=self.model,
                    messages=messages,
                    options={
                        'temperature': temperature,
                    },
                    stream=stream
                )
                
                reply = response['message']['content']
                
                # Update history
                self.conversation_history.append({'role': 'user', 'content': message})
                self.conversation_history.append({'role': 'assistant', 'content': reply})
                
                return reply
            
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    return None
    
    def clear_history(self):
        """Reset conversation."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict]:
        """Get conversation history."""
        return self.conversation_history.copy()

# Example usage
if __name__ == '__main__':
    client = OllamaClient(model='gemma2:9b')
    
    response = client.chat(
        message="What's the capital of France?",
        system_prompt="You are a helpful geography assistant."
    )
    
    print(response)
    
    # Follow-up (uses history)
    response = client.chat("What's its population?")
    print(response)
