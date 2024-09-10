import requests
import json

url = "http://api.open-notify.org/iss-now.json"
header= {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
}

data = requests.get(url,headers=header)

response = requests.get(url)

print(response)

if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()

    # Printing the JSON response
    print("JSON Response:", data)
else:
    print("Failed to retrieve data. Status Code:", response.status_code)