import json
import requests
#TODO: ADD ERROR LOGGING
#TODO: delete whatever can leave
BASE_URL = "https://openlibrary.org"

def search_for_author(search): #get thet author and info
    print(f"Searching for author...")
    response = requests.get(f"{BASE_URL}/search/authors.json", params= {"q": search, "limit": 5})
    data = response.json()
    return data["docs"]

def show_author_works(author_code): #get the authors work shown
    response = requests.get(f"{BASE_URL}/authors/{author_code}/works.json", params={"limit": 5})
    data = response.json()
    return data["entries"]


#author_chosen = (search_for_author(author_choice))
#first = author_chosen[0]

#author = first.get("name")
#author_book_count = first.get("work_count")
#author_top_work = first.get("top_work")

#print(f" Author: {author}, work count: {author_book_count}, top_work: {author_top_work} ")

#key = first.get("key")
#author_works = show_author_works(key)

#for title in author_works:
    print("-", title.get("title"))

#print(f" Author: {author}, works: {len(author_works)} ")