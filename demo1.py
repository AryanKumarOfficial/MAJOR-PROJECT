import http.client

conn = http.client.HTTPSConnection("api.scrapingant.com")

url="https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=b10e6edf-e0b8-4364-8437-45e11ae5ab89.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=o9pb8jsue80000001713774872831&qH=0b3f45b266a97d70"

conn.request("GET", f"/v2/general?url=${url}&x-api-key=00fd0fc814e44a07b06ced7aba3d331f")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))