import requests
import json
def downloadFlag(country):
    with open(country+'.png', 'wb') as handle:
        if data.get(country) is None:
            print("Flag not found. Deepest apologies.")
        else:
            img_data = requests.get(data.get(country)).content
            handle.write(img_data)
    


with open('token.txt', 'r') as file:
    token = file.read()

emojis_url = 'https://api.github.com/emojis'

params = dict(username="tomasbutkevicius",password=token)

resp = requests.get(url=emojis_url, params=params)
data=resp.json()

country = input("Enter country name of flag to download: ")
downloadFlag(country.lower())
