import json
import requests

# Let's steal the api key :D
with open('config.json') as f:
    config = json.load(f)
    api_key = config.get('api_key', '')  # NO API KEY? STRING EMPTY

if not api_key:
    # No api key???
    api_key = input("Enter API key: ")
    with open('config.json', 'w') as f:
        json.dump({'api_key': api_key}, f)
while True:
    ip_address = input("Enter IP address to check: ")

    # Dat a vpn? or dat not a vpn
    url = f"https://vpnapi.io/api/{ip_address}?key={api_key}"
    response = requests.get(url).json()

    # save that shit 
    with open('data.json', 'a') as f:
        json.dump({"response": response}, f)
        f.write('\n') #o shit, not gud

    # Prints the check
    print(response)
    break

