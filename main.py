import requests
import pandas as pd

url = "https://everycoffee.vercel.app/api/getMoreCoffees"

x = 1


scraped_coffees = []
while True:

  querystring = {"page":f"{x}","limit":"1000"}
  headers = {
      "authority": "everycoffee.vercel.app",
      "accept": "*/*",
      "accept-language": "en-US,en;q=0.9",
      "if-none-match": "W/^\^yq7csf4wd62mq1^^",
      "referer": "https://everycoffee.vercel.app/",
      "sec-ch-ua": "^\^Chromium^^;v=^\^118^^, ^\^Google",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "^\^Windows^^",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.json()
  if len(data) == 0:
    break

  x += 1
  print(f"Scraped {len(data)} coffees from page {x-1}.")
  scraped_coffees.extend(data)

print(f"Total coffees scraped: {len(scraped_coffees)}")

dataframe = pd.json_normalize(scraped_coffees)
dataframe.to_csv("scraped_coffees.csv", index=False)

print("Check out the scraped coffee csv file!")
