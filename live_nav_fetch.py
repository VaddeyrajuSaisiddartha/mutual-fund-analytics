print("STARTING SCRIPT")
import requests
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Mutual Fund Schemes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("Fetching NAV Data...\n")

for scheme_name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if "data" in data:

                df = pd.DataFrame(data["data"])

                file_name = f"data/raw/{scheme_name}_NAV.csv"

                df.to_csv(file_name, index=False)

                print(f"SUCCESS: {scheme_name} saved to {file_name}")

            else:
                print(f"ERROR: No NAV data found for {scheme_name}")

        else:
            print(f"ERROR: API returned status {response.status_code} for {scheme_name}")

    except Exception as e:
        print(f"ERROR: {scheme_name} -> {e}")

print("\nNAV Fetch Completed!")
                                            