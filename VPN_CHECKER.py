import json
import requests
import os
os.system("title " + "VPN Check tool - Github.com/Realzuko")
with open('config.json') as j:
    config = json.load(j)
    api_key = config.get('api_key', '')  # Check if the API key is empty or not.
if not api_key:
    # If no api key, that will ask for the API key and save it to config.json
    api_key = input("Enter API key: ")
    with open('config.json', 'w') as f:
        json.dump({'api_key': api_key}, f)
ip_address = input("Enter IP address to check: ")

# 
url = f"https://vpnapi.io/api/{ip_address}?key={api_key}"
response = requests.get(url).json()

#save data to a data.json file
with open('data.json', 'a') as f:
    json.dump({"response": response}, f)
    print(response) # Print The Response

