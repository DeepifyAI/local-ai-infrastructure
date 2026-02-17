#!/usr/bin/env python3
import json

def save_conversation(agent, filename):
    with open(filename, 'w') as f:
        json.dump(agent.messages, f)

def load_conversation(agent, filename):
    with open(filename) as f:
        agent.messages = json.load(f)
