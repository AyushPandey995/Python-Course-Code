import requests

url = "https://api.github.com/users/octocat"  
response = requests.get(url)
print(response.text)

with open ("file_detail.txt", "w") as f:
    f.write(response.text)
   
