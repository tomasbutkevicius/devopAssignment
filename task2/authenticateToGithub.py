import requests
import json

with open('username.txt', 'r') as file:
    username = file.read()

with open('token.txt', 'r') as file:
    token = file.read()

repos_url = 'https://api.github.com/user/repos'

gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me to check if authentication worked
repos = json.loads(gh_session.get(repos_url).text)

for repo in repos:
    print(repo["name"])
    
