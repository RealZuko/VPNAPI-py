import json
import requests
import os

os.system("title " + "VPN Check tool - Github.com/Realzuko")

# Load the API key from config.json file
with open('config.json') as j:
    config = json.load(j)
    api_key = config.get('api_key', '')

# If the API key is empty, ask for the API key and save it to config.json file
if not api_key:
    api_key = input("Enter API key: ")
    with open('config.json', 'w') as f:
        json.dump({'api_key': api_key}, f)

# ask for ip user input
ip_address = input("Enter IP address to check: ")

# Call the VPN API to get the response
url = f"https://vpnapi.io/api/{ip_address}?key={api_key}"
response = requests.get(url).json()

# Extract the relevant information from the response
ip_given = response.get('ip', '')
vpn_proxy = response.get('security', {}).get('vpn', False) or response.get('security', {}).get('proxy', False)
isp = response.get('network', {}).get('autonomous_system_organization', '')

# Print the extracted information
print(f"IP Given: {ip_given}")
print(f"VPN/Proxy: {vpn_proxy}")
print(f"ISP: {isp}")
print("More specific data was saved to data.json, look for " + ip_address)
