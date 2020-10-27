import requests
import json
def downloadFlag(country):        
    if data.get(country) is None:
        print("Flag not found. Deepest apologies.")
    else:
        with open(country + '.png', 'wb') as handle:
            img_data = requests.get(data.get(country)).content
            handle.write(img_data)
    

emojis_url = 'https://api.github.com/emojis'

resp = requests.get(url = emojis_url)
data=resp.json()

country = input("Enter country name of flag to download: ")
downloadFlag(country.lower())
