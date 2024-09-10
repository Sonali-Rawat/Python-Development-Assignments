import requests
import pandas as pd
import time


url = "http://api.open-notify.org/iss-now.json"

header= {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
}

iss_data = []  # Ensure this is declared before use

# Loop to get 100 records
for i in range(100):
    try:
        # Sending a GET request to fetch ISS location data
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parsing the JSON response
            data = response.json()
            
            # Extracting latitude, longitude, and timestamp
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            timestamp = data['timestamp']
            
            # Appending the data to the list
            iss_data.append({
                'timestamp': timestamp,
                'latitude': latitude,
                'longitude': longitude
            })
            
            # Printing progress
            print(f"Record {i + 1} collected: {latitude}, {longitude} at {timestamp}")
        else:
            print(f"Failed to retrieve data for record {i + 1}, Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Pause for 1 second before fetching the next record to avoid hitting API rate limits
    time.sleep(1)

# Check if any data was collected before writing to CSV
if len(iss_data) > 0:
    # Creating a DataFrame from the collected data
    df = pd.DataFrame(iss_data)

    # Writing the data to a CSV file
    df.to_csv(r'iss_location_data.csv', index=False)  # Adjust the path if necessary

    print("Data successfully written to 'iss_location_data.csv'")
else:
    print("No data was collected.")



    