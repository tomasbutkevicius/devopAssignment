import requests
import json

username = 'tomasbutkevicius'

# from https://github.com/user/settings/tokens
with open('token.txt', 'r') as file:
    token = file.read()

repos_url = 'https://api.github.com/user/repos'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me to check if authentication worked
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names
for repo in repos:
    print(repo["name"])
    
