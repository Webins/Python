import requests as response

url = "https://icanhazdadjoke.com"

r = response.get(url, headers={"Accept":"application/json"})

print(f"your request to {url} came back with status code: {r.status_code}")

#print(r.text) #string

data = r.json() #dict

print(data["joke"]) 