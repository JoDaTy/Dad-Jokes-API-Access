# Dad-Jokes-API-Access

A Jenkins job to run a Python script that accesses the Dad Jokes API. Below is a step-by-step guide to help you set this up:

## Prerequisites

Jenkins Installed: Ensure you have Jenkins installed and running on your machine or server.
Python Installed: Ensure Python is installed on the Jenkins server.
Dad Jokes API Access: You will be using a public API, so no special authentication is required.

## Step-by-Step Guide

Step 1: Install Necessary Jenkins Plugins

Python Plugin: Install the Python plugin (if necessary) to ensure Jenkins can run Python scripts. Go to Manage Jenkins -> Manage Plugins -> Available and search for "Python Plugin" to install it.

Step 2: Prepare Your Python Script

Create a Script: 

import requests

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        joke = response.json().get("joke")
        print(f"Dad Joke: {joke}")
    else:
        print("Failed to fetch a dad joke.")

if __name__ == "__main__":
    get_dad_joke()

## Dependencies: 

External libraries (like requests), ensure they are listed in a requirements.txt file.
