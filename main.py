import requests, secrets

playerUsername = "TechnoBlade"
api_path = "https://api.hypixel.net/v2/skyblock/bazaar"
url = api_path+f'?key={secrets.HYPIXEL_API_KEY}&name={playerUsername}'

print(requests.get(url).json())