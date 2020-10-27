import requests
import json
import subprocess

def cloneToSystem(clone_url):
    subprocess.call('git clone ' + clone_url, shell = True)

print("CLONE REPOSITORY")
user = input("Enter owner name of repository: ")
repo = input("Enter repository name: ")

repository_url = 'https://api.github.com/repos/' + user + '/' + repo

resp = requests.get(url = repository_url)
data = resp.json()

if data.get("message") == "Not Found":
    print("repository not found")
else:
    cloneToSystem(data.get("clone_url"))
