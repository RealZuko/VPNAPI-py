import json
import requests
import os
# Let's steal the api key :D
os.system("title " + "VPN Check tool - Github.com/Realzuko")
with open('config.json') as j:
    config = json.load(j)
    api_key = config.get('api_key', '')  # NO API KEY? STRING EMPTY

if not api_key:
    # No api key???
    api_key = input("Enter API key: ")
    with open('config.json', 'w') as f:
        json.dump({'api_key': api_key}, f)
ip_address = input("Enter IP address to check: ")

# Dat a vpn? or dat not a vpn
url = f"https://vpnapi.io/api/{ip_address}?key={api_key}"
response = requests.get(url).json()

    # save that shit 
with open('data.json', 'a') as f:
    json.dump({"response": response}, f)
    print(response) #made it more readable ,because it was slightly annoying.

