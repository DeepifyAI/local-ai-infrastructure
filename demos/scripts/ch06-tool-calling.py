#!/usr/bin/env python3
"""Chapter 6: AI that can use tools (function calling)."""
import json
from datetime import datetime
from ollama import chat

def get_current_time():
    """Get the current date and time."""
    return datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")

def calculate(expression):
    """Evaluate a math expression safely."""
    allowed = set("0123456789+-*/.(). ")
    if all(c in allowed for c in expression):
        return str(eval(expression))
    return "Invalid expression"

tools = [
    {"type": "function", "function": {
        "name": "get_current_time",
        "description": "Get the current date and time",
        "parameters": {"type": "object", "properties": {}}
    }},
    {"type": "function", "function": {
        "name": "calculate",
        "description": "Calculate a math expression",
        "parameters": {"type": "object", "properties": {
            "expression": {"type": "string", "description": "Math expression to evaluate"}
        }, "required": ["expression"]}
    }}
]

print("=== AI with Tools (Function Calling) ===")
print()

questions = [
    "What time is it right now?",
    "What is 1024 * 768?",
]

for q in questions:
    print(f"You: {q}")
    response = chat(
        model="gemma2:9b",
        messages=[{"role": "user", "content": q}],
        tools=tools
    )
    
    msg = response["message"]
    if msg.get("tool_calls"):
        for tc in msg["tool_calls"]:
            fn = tc["function"]["name"]
            args = tc["function"]["arguments"]
            print(f"  🔧 Calling: {fn}({args})")
            
            if fn == "get_current_time":
                result = get_current_time()
            elif fn == "calculate":
                result = calculate(args.get("expression", ""))
            else:
                result = "Unknown tool"
            print(f"  📋 Result: {result}")
    else:
        answer = msg["content"][:150]
        print(f"AI:  {answer}")
    print()

print("The model decided WHICH tool to call and HOW. All locally.")
