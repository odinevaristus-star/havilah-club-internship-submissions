# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (optional for this public API).
API_KEY = os.getenv("API_KEY", "")
# Using JSONPlaceholder Users API (Free public API, no key required)
BASE_URL = "https://jsonplaceholder.typicode.com/users"


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    try:
        # If the user enters a number, search by user ID; otherwise fetch all
        params = {"id": query} if query.isdigit() else {}
        response = requests.get(BASE_URL, params=params)
        
        # Check response.status_code before calling .json()
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    if not data:
        print("No data found to display.")
        return

    # Handle both list and dictionary responses
    if isinstance(data, list):
        if len(data) == 0:
            print("No results found for your query.")
            return
        user = data[0]
    else:
        user = data

    print("\n=== User Profile Details ===")
    print(f"  • Name:     {user.get('name', 'N/A')}")
    print(f"  • Username: {user.get('username', 'N/A')}")
    print(f"  • Email:    {user.get('email', 'N/A')}")
    print(f"  • City:     {user.get('address', {}).get('city', 'N/A')}")
    print(f"  • Company:  {user.get('company', {}).get('name', 'N/A')}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Tip: You can enter a user ID between 1 and 10 (e.g., 1, 3, 5).")
    query = input("Enter your search query (User ID): ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()