import json
import pandas as pd
from fuzzywuzzy import fuzz

# Load FAQ data
with open("faq_data.json", "r") as f:
    faq = json.load(f)

def find_best_answer(user_input):
    best_match = None
    highest_score = 0
    for item in faq:
        score = fuzz.ratio(user_input.lower(), item["question"].lower())
        if score > highest_score:
            highest_score = score
            best_match = item
    if highest_score > 60:
        return best_match["answer"]
    return "Sorry, I couldn't find an answer. Please ask a different question."

# Example usage:
if __name__ == "__main__":
    while True:
        query = input("Ask me: ")
        print(find_best_answer(query))