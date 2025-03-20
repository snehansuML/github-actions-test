import requests
import json

# Fetch live Bitcoin price from a free API
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    data = response.json()

    # Extract relevant data
    bitcoin_price = data["bpi"]["USD"]["rate"]
    print(f"✅ Current Bitcoin Price: ${bitcoin_price}")

    # Save the data to a file
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Data saved to output.json successfully!")

except Exception as e:
    print(f"❌ Error fetching data: {e}")
