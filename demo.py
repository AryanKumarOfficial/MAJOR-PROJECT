from parser import fetchAndSaveToFile
import time

for i in range(1,182+1):
    fetchAndSaveToFile(f"https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page={i}",f"data/flipkart_iphone_{i}.html" )
    time.sleep(1)
    