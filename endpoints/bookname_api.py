import json
import requests

BASE_URL = "https://openlibrary.org"

def search_book(title):
    print("searching book " + title)
    response = requests.get(f"{BASE_URL}/search.json", params={"title": title, "limit": 5} )
    data = response.json()
    return data["docs"]

