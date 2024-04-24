import requests

url = "https://api.scrapingant.com/v2/general" #proxy url


target_url  ="https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=b10e6edf-e0b8-4364-8437-45e11ae5ab89.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=o9pb8jsue80000001713774872831&qH=0b3f45b266a97d70" #product url


proxies ={
   "http" :"20.204.190.254:3129",
   "https": "20.219.178.121:3129",
}


params = {
    "url": target_url,
    "x-api-key": "00fd0fc814e44a07b06ced7aba3d331f",
    "render_js": "false",
    "proxy": proxies
}



def fetchAndSaveToFile(url,path):
    try:
        print("Fetching data from ",url)
        r= requests.get(url,params=params)
        with open(path, "w",encoding="utf-8") as f:
                # print(r.text)
                f.write(r.text)
        print("Data saved to ",path)


    except Exception as e:
        print("Error fetching data from ",url)
        print(e)
        return


fetchAndSaveToFile(url,"data/flipkart_iphone.html" )