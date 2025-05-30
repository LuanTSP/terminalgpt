from openai import OpenAI
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Read API key
path = os.path.join(os.path.dirname(__file__), 'api_key.txt')
API_KEY = open(path, "r").read().strip()
client = OpenAI(api_key=API_KEY)

# Conversation history
messages = []

# Welcome message
print(Fore.BLUE + Style.BRIGHT + "\n----------- Welcome to GPT -----------")
print(Style.RESET_ALL + "Type 'exit' to quit")

while True:
    try:
        # Get user input
        text = input(f'\n{Fore.BLUE + Style.BRIGHT}[USER]: {Fore.GREEN + Style.BRIGHT}')
        if text.strip().lower() == 'exit':
            break

        # Append user message
        messages.append({"role": "user", "content": text})

        # Send request
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages
        )

        # Extract assistant message
        assistant_msg = response.choices[0].message
        messages.append(assistant_msg)

        # Print response
        print(f'{Fore.RED + Style.BRIGHT}[GPT]: {Fore.WHITE + Style.BRIGHT}{assistant_msg.content}')

        # Print usage
        print(Style.DIM + f"Tokens used: {response.usage.total_tokens}")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\n[ERROR]: {e}")
