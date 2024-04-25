import requests
from bs4 import BeautifulSoup
from collections import Counter

with open("data/flipkart_iphone.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Extract title
title = soup.find("title").string
print(title)

# Find all comments
comments = soup.find_all("div", class_="RcXBOT")

# Initialize Counter to count word occurrences
word_counter = Counter()

# Iterate over comments
for comment in comments:
    # Extract text from paragraph tag
    comment_text = comment.find("p")
    if comment_text is None:
        continue
    comment_text = comment_text.text
    
    # Split text into words and update word counter
    word_counter.update(comment_text.split())

# Filter out words with zero occurrences
word_counter = {word: count for word, count in word_counter.items() if count > 0}

# rearrange the dictionary in descending order of frequency

word_counter = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)

final = dict(word_counter)

print(final)
