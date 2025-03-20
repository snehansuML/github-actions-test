import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    data = response.json()

    # Extract Bitcoin price
    bitcoin_price = data["bpi"]["USD"]["rate"]
    print(f"✅ Current Bitcoin Price: ${bitcoin_price}")

    # Ensure output.json exists
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Data saved to output.json successfully!")

except Exception as e:
    print(f"❌ Error fetching data: {e}")

# Force create output.json if empty
with open("output.json", "a") as f:
    pass  # This ensures the file exists
