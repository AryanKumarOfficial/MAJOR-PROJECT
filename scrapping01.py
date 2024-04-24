import requests
from bs4 import BeautifulSoup

with open("data/flipkart_iphone.html", "r",encoding="utf-8") as file:
    html = file.read()
    
soup = BeautifulSoup(html, "html.parser")

title = soup.find("title").string

comments  = soup.find_all("div", class_="RcXBOT")

print(title)

for comment in comments:
   for c in comment.find_all("p"):
       print(c.string)
    