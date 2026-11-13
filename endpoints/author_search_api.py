import json
import requests
BASE_URL = "https://openlibrary.org"

def search_for_author_with_api(search): #get thet author and info
    print(f"Searching for author...")
    response = requests.get(f"{BASE_URL}/search/authors.json", params= {"q": search, "limit": 5})
    data = response.json()
    return data["docs"]

def show_author_works_with_api(author_code): #get the authors work shown
    response = requests.get(f"{BASE_URL}/authors/{author_code}/works.json", params={"limit": 5})
    data = response.json()
    return data["entries"]