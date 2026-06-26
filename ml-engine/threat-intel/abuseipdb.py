import requests

API_KEY = "4ea25443c8354bc49af5c885c61017ea5431d12cefaf2b17bedb50466367c82ae8c850c97db263ae"

ip = "8.8.8.8"

url = "https://api.abuseipdb.com/api/v2/check"

headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

params = {
    "ipAddress": ip,
    "maxAgeInDays": 90
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print(response.json())