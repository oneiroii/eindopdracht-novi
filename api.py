import json
import requests

def search_book(book_search_query, field):
    print("searching book " + book_search_query)
    api_response = requests.get(
        "https://openlibrary.org/search.json",
        params={"q": book_search_query, "fields": field},
    )
    api_response.raise_for_status()  # stops with a clear error if the request failed (e.g. 404/500)
    return api_response.json()