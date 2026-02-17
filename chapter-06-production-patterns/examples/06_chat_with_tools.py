#!/usr/bin/env python3
import ollama
import json

# Define available tools
tools = {
    'get_weather': lambda city: f"Weather in {city}: 72°F, sunny",
    'search_web': lambda query: f"Top result for '{query}': LocalAI.dev",
}

# Very strict system prompt for tool use
system = """You are a tool-calling assistant. When the user asks something that requires a tool, respond ONLY with valid JSON like this:
{"tool": "get_weather", "args": {"city": "London"}}

Available tools:
- get_weather(city): Get current weather
- search_web(query): Search the web

No other text. JSON only."""

def chat_with_tools(user_message):
    print(f"User: {user_message}")
    
    response = ollama.chat(model='gemma2:9b', messages=[
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': user_message}
    ])
    
    content = response['message']['content'].strip()
    
    # Strip markdown fences if present
    if content.startswith('```'):
        lines = content.split('\n')
        content = '\n'.join(lines[1:-1] if lines[-1].strip() == '```' else lines[1:])
    
    # Try tool call
    if '{' in content and '"tool"' in content:
        try:
            # Extract JSON from content
            start = content.index('{')
            end = content.rindex('}') + 1
            tool_call = json.loads(content[start:end])
            tool_name = tool_call['tool']
            args = tool_call.get('args', {})
            
            print(f"→ Model calls tool: {tool_name}({args})")
            result = tools[tool_name](**args)
            print(f"→ Tool result: {result}")
            
            # Send result back
            final = ollama.chat(model='gemma2:9b', messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': user_message},
                {'role': 'assistant', 'content': content},
                {'role': 'user', 'content': f'Tool result: {result}. Now answer the user.'}
            ])
            print(f"Assistant: {final['message']['content']}")
            return
        except Exception as e:
            pass  # Fall through to direct response
    
    print(f"Assistant: {content}")

if __name__ == '__main__':
    print("=== Tool Calling Demo ===\n")
    chat_with_tools("What's the weather in London?")
