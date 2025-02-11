import requests
import json
from datetime import datetime
categories=["sports","general","business","weather","money"]
print("Which category of news do u want.?")
for i,category in enumerate(categories,start=1):
  print(f"{i}.{category}")

choice=int(input("Your choice of news>?"))
if choice>=1 and choice<len(categories):
  selectednews=categories[choice -1]
current_time=datetime.now().strftime("%Y %m %D")
url=f"https://newsapi.org/v2/everything?q={selectednews}&from={current_time}&sortBy=publishedAt&apiKey=67cd104f146e476086f7b5b09b8183e8"
r=requests.get(url)
try:
    if r.status_code==200:
     news=json.loads(r.text)
     print(news)
     print(type(news))


     for article in news["articles"]:
      print(article["title"])
      print(article["description"])
      print("-----------------")
except:
  print(f"FAILED TO FETCH NEWS!")

