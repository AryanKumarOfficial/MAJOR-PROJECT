import requests
from bs4 import BeautifulSoup
from collections import Counter

with open("data/flipkart_iphone_1.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Extract title
title = soup.find("title").string
print(title)

# Find all comments
review_section = soup.find("span", class_="Wphh3N")
comments_section = soup.find_all("div", class_="ZmyHeo")



total_reviews = review_section.findChildren("span", recursive=False)[-1].contents[-1].string

# print(total_reviews)

# print(type(comments_section))

all_words = []

for comment in comments_section:
    unwanted = comment.find("span", class_="wTYmpv")
    if unwanted:
        unwanted.decompose()
    comment_text = comment.get_text()
    comment_text = comment_text.strip()
    all_words.extend(comment_text.split())
    
  

print(all_words)
