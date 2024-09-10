import requests


url = "http://api.open-notify.org/iss-now.json"
header= {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url, headers=header)

if response.status_code == 200:
   
    data = response.json()

    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")
else:
    print("Failed to retrieve data. Status Code:", response.status_code)
