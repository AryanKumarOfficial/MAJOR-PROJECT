url = "www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page=1"

if f"https://" in url:
    print(url.split("/")[3])
else:
    print(url.split("/")[1])
