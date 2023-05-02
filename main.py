import json
import requests
import os

os.system("title " + "VPN Check tool - Github.com/Realzuko")

# Load the API key from config.json file
with open('config.json') as j:
    config = json.load(j)
    api_key = config.get('api_key', '')

# If the API key is empty or set to "PLACE_API_KEY_HERE", ask for the API key and save it to config.json file
if not api_key or api_key == "ENTER_API_KEY_HERE":
    api_key = input("Enter API key: ")
    with open('config.json', 'w') as f:
        json.dump({'api_key': api_key}, f)


# Get the IP address from user input
ip_address = input("Enter IP address to check: ")

# Call the VPN API to get the response
url = f"https://vpnapi.io/api/{ip_address}?key={api_key}"
response = requests.get(url).json()

# Extract the relevant information from the response
ip_given = response.get('ip', '')
vpn_proxy = response.get('security', {}).get('vpn', False) or response.get('security', {}).get('proxy', False)
isp = response.get('network', {}).get('autonomous_system_organization', '')


# Create a new directory to save the JSON files
if not os.path.exists('Results'):
    os.makedirs('Results')

# Save the response to a file named after the IP address
filename = f"Results/{ip_given}.json"
with open(filename, 'w') as f:
    json.dump(response, f, indent=1)

# Extract the relevant information from the response
ip_given = response.get('ip', '')
vpn_proxy = response.get('security', {}).get('vpn', False) or response.get('security', {}).get('proxy', False)
isp = response.get('network', {}).get('autonomous_system_organization', '')

# Print the extracted information
print(f"IP Given: {ip_given}")
print(f"VPN/Proxy: {vpn_proxy}")
print(f"ISP: {isp}")
print(f"More specific data was saved to {filename}")
