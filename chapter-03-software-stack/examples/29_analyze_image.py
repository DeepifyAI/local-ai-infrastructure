#!/usr/bin/env python3
# vision_demo.py
"""
Local image analysis with LLaVA.
"""

from ollama import chat
import base64

def analyze_image(image_path: str, prompt: str = "Describe this image in detail.") -> str:
    """Analyze an image with a local vision model."""
    
    # Read and encode image
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    # Call vision model
    response = chat(
        model='llava:7b',  # or llama3.2-vision:11b
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [image_data]
        }]
    )
    
    return response['message']['content']

if __name__ == '__main__':
    # First, pull vision model
    import os
    os.system('ollama pull llava:7b')
    
    # Analyze an image
    description = analyze_image('photo.jpg', "What's in this image?")
    print(description)
