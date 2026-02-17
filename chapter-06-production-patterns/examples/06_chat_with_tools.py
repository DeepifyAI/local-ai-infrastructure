#!/usr/bin/env python3
import ollama
import json

# Define available tools
tools = {
    'get_weather': lambda city: f"Weather in {city}: 72°F, sunny",
    'search_web': lambda query: f"Top result for '{query}': Example.com",
}

# System prompt explaining tools
system = """
You have access to these tools:
- get_weather(city): Get current weather
- search_web(query): Search the web

To use a tool, output JSON: {"tool": "tool_name", "args": {"arg": "value"}}
"""

def chat_with_tools(user_message):
    response = ollama.chat(model='gemma2:9b', messages=[
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': user_message}
    ])
    
    content = response['message']['content']
    
    # Check if model wants to use a tool
    if content.strip().startswith('{'):
        try:
            tool_call = json.loads(content)
            tool_name = tool_call['tool']
            args = tool_call['args']
            
            # Execute tool
            result = tools[tool_name](**args)
            
            # Send result back to model
            return ollama.chat(model='gemma2:9b', messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user_message},
                {'role': 'assistant', 'content': content},
                {'role': 'user', 'content': f'Tool result: {result}'}
            ])['message']['content']
        except:
            return "Tool call failed"
    
    return content

print(chat_with_tools("What's the weather in London?"))
