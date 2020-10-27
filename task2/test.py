import requests
import os
 
# Getting user input
unix_user = input("Enter your Unix username: ")
github_user = input("Enter your GitHub username: ")
 
# Making sure .ssh directory exists and opening authorized_keys file
ssh_dir = '/home/'+unix_user+'/.ssh/'
if not os.path.exists(ssh_dir):
    os.makedirs(ssh_dir)
 
authorized_keys_file = open(ssh_dir+'authorized_keys','a')
 
# Sending a request to the GiHub API and storing the response in a variable named'response'
api_root = "https://api.github.com"
request_header = {'Accept':'application/vnd.github.v3+json'}
response = requests.get(api_root+'/users/'+github_user+'/keys', headers = request_header)
 
## Processing the response and appending keys to authorized_keys file
for i in response.json():
    authorized_keys_file.write(i['key']+'\n')
