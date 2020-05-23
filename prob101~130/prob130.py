import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
width=max_price - min_price
x=opening_price + width

if x>max_price:
    print("상승장")

else:
    print("하락장")
