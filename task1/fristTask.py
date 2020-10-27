import urllib.request, json 
with urllib.request.urlopen("https://api.github.com/") as url:
    data = json.loads(url.read().decode())
    
print(data)
data = json.dumps(data) 
data = data[1:]
data = data[:-1]

allMethods = data.split('",')

    
    
allMethods = allMethods[:-1]
with open("AllPossibleGitHubAPI.txt", "w") as outputFile:
    for line in allMethods:
        line =  line + '"'
        print(line, file=outputFile)
        
with open("AllPossibleGitHubAPI_noparameters.txt", "w") as outputFile:
    for line in allMethods:
        line =  line + '"'
        if "{" not in line: 
            print(line, file=outputFile)
            
with open("AllPossibleGitHubAPI_requireparameters.txt", "w") as outputFile:
    for line in allMethods:
        line =  line + '"'
        if "{" in line: 
            print(line, file=outputFile)
