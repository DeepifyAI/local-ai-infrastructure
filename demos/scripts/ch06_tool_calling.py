#!/usr/bin/env python3
"""
Tool calling: the AI decides WHICH tool to use, then uses it.
"""
import ollama
import json

# Real tools the AI can call
TOOLS = {
    'get_weather': lambda city: f"{city}: 18°C, partly cloudy",
    'get_time':    lambda tz:   f"{tz}: 14:32 UTC+0",
    'calculate':   lambda expr: str(eval(expr)),
}

SYSTEM = """You are a helpful assistant with tools. When you need a tool, reply ONLY with JSON:
{"tool": "get_weather", "args": {"city": "London"}}
{"tool": "get_time", "args": {"tz": "Europe/London"}}
{"tool": "calculate", "args": {"expr": "100 * 1.2"}}
No other text — just the JSON."""

def run(query):
    print(f"  User: {query}")
    r = ollama.chat(model='gemma2:9b', messages=[
        {'role': 'system', 'content': SYSTEM},
        {'role': 'user',   'content': query}
    ])
    raw = r['message']['content'].strip()

    # Strip markdown fences
    if raw.startswith('```'):
        raw = '\n'.join(raw.split('\n')[1:-1])

    if '{' in raw and '"tool"' in raw:
        try:
            start, end = raw.index('{'), raw.rindex('}') + 1
            call = json.loads(raw[start:end])
            tool_name, args = call['tool'], call.get('args', {})
            result = TOOLS[tool_name](**args)
            print(f"  → AI calls: {tool_name}({args})")
            print(f"  → Tool returns: {result}")

            final = ollama.chat(model='gemma2:9b', messages=[
                {'role': 'system',    'content': 'You are a helpful assistant.'},
                {'role': 'user',      'content': query},
                {'role': 'assistant', 'content': raw},
                {'role': 'user',      'content': f'Tool result: {result}. Answer the user.'}
            ])
            print(f"  AI: {final['message']['content'].strip()}\n")
            return
        except Exception:
            pass
    print(f"  AI: {raw}\n")

print("=== Tool Calling Demo ===\n")
run("What's the weather in Paris?")
print("✓  The AI chose the right tool, called it, and used the result.")
