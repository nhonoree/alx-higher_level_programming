#!/usr/bin/python3
"""
Search API script:
Sends a POST request to a given URL with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # URL to send the POST request to
    url = "http://0.0.0.0:5000/search_user"
    
    # Retrieve the letter from command-line arguments or set q=""
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    
    try:
        # Send POST request
        response = requests.post(url, data=payload)
        response_json = response.json()

        # Check if the JSON response is not empty
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
