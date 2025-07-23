import os
import json
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    local_path = os.path.join(os.getcwd(), "ai.json")
    fallback_path = os.path.join(os.getcwd(), "src", "ai.json")

    if os.path.exists(local_path):
        file = local_path
    elif os.path.exists(fallback_path):
        file = fallback_path
    else:
        print(f"Usage: {sys.argv[0]} ai.json \nExiting...")
        exit()

try:
    with open(file, "r") as jsonfile:
        responses = json.load(jsonfile)
except Exception as e:
    print(f"AI: Failed to load JSON file: {e}")
    exit()

print("Basic AI Chatbot. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()
    
    if user_input in ["exit", "quit", "stop"]:
        print("AI: Goodbye!")
        break

    found = False
    for keyword in responses:
        if keyword in user_input:
            print(f"AI: {responses[keyword]}")
            found = True
            break

    if not found:
        print("AI: I'm not sure how to respond to that. Can you ask something else?")
