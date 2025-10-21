# random_facts.py
# A small Python script that prints a random fun fact each time you run it.

import random

facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts and blue blood.",
    "The shortest war in history lasted 38 minutes (Anglo-Zanzibar War, 1896).",
    "A day on Venus is longer than a year on Venus."
]

def show_random_fact():
    fact = random.choice(facts)
    print("💡 Random Fact of the Day:")
    print(fact)

if __name__ == "__main__":
    show_random_fact()
    
# hi