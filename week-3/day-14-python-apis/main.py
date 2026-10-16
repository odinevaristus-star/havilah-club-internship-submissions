# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
def fetch_data(query):
    if not API_KEY:
        print("Error: API_KEY is missing. Please check your .env configuration.")
        return None

    params = {
        "q": query,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("Error: Invalid API Key. Please verify your key in the .env file.")
        elif response.status_code == 404:
            print(f"Error: Location '{query}' not found. Please try another search query.")
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        
    return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
def display_results(data):
    try:
        city = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        description = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print("\n" + "="*45)
        print(f"      WEATHER REPORT FOR {city.upper()}, {country}")
        print("="*45)
        print(f"  • Condition   : {description}")
        print(f"  • Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f"  • Humidity    : {humidity}%")
        print("="*45 + "\n")
        
    except (KeyError, IndexError) as e:
        print(f"Error parsing the API response structure: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    query = input("Enter city name for weather search: ").strip()
    if query:
        data = fetch_data(query)
        if data:
            display_results(data)
    else:
        print("Search query cannot be empty.")


if __name__ == "__main__":
    main()