# APIKEY 
import openai
import os
from colorama import Fore, Style

# get api key
path = os.path.join(os.path.dirname(__file__), 'api_key.txt')
API_KEY=open(path, "r").read()

openai.api_key = API_KEY
messages = []

print(Fore.BLUE + Style.BRIGHT + "\n-----------Welcome to GPT-----------")
print(Style.RESET_ALL + "Type 'exit' to exit")
while True:
    text = input(f'\n{Fore.BLUE + Style.BRIGHT + "[USER]"}:{Fore.GREEN + Style.BRIGHT + " "}')
    if text == 'exit':
        break

    # making message
    dic = {"role": "user", "content": text}
    messages.append(dic)

    # getting response
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )

    # getting usage
    usage = response['usage']['total_tokens']

    # appending to context of conversation
    response_dic = response['choices'][-1]['message']
    messages.append(response_dic)

    # getting response text
    response_text = response_dic['content']
    print(f'{Fore.RED + Style.BRIGHT + "[GPT]"}: {Fore.WHITE + Style.BRIGHT + response_text}')
    print(Style.RESET_ALL + f"usage: {usage}")


