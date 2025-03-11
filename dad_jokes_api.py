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
