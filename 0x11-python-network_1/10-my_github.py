#!/usr/bin/python3
"""
GitHub API script:
Displays the user's GitHub id using Basic Authentication.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if sufficient arguments are passed
    if len(sys.argv) < 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    # Get username and token
    username = sys.argv[1]
    token = sys.argv[2]

    # URL for GitHub API user endpoint
    url = "https://api.github.com/user"
    
    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))
    
    # Parse and display the user id or None
    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")
