import requests
import json



with open('token.txt', 'r') as file:
    token = file.read()

emojis_url = 'https://api.github.com/emojis'

params = dict(username="tomasbutkevicius",password=token)

resp = requests.get(url=emojis_url, params=params)
data=resp.json()


print(data.get("lithuania"))


    
