#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Send the GET request to GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for i in range(10):
            sha = commits[i]['sha']
            author = commits[i]['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("Error fetching commits")
