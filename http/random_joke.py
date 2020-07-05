import requests as r
from random import choice
from pyfiglet import figlet_format as ff
from termcolor import colored

print(colored(ff("Random Joke"), color="cyan", attrs=["blink"]))

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
response = r.get(
    url, 
    headers={"Accept":"application/json"},
    params={"term": topic}
).json()

size = response["total_jokes"]
data = response["results"]


if size > 1: 
    print(f"I've got {size} joke about {topic} Here it is one:\n")
    print(colored(choice(data)["joke"], color="cyan"))
    print()
elif size == 1:
    print(f"I have only one joke about {topic}. Here it is:")
    print(colored(data[0]["joke"], color="cyan"))
    print()
else:
    print(colored("\nSorry i dind't find any joke about " + topic + ". Try again!", color="red"))
    print()

