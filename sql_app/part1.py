import json
import requests
from bs4 import BeautifulSoup
import database 
import models, main

db = database.SessionLocal()


def wiki_repseonse(topic):
    URL = f"https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}"
    response_API = requests.get(URL)
    package_response = json.loads(response_API.text).get("parse")

    title = package_response.get("title")
    text = package_response.get("text").get("*")
    soup = BeautifulSoup(text, "html.parser")

    count = 0
    for page in soup.findAll('p'):
        count += page.getText().count(title)
    
    Wiki_page = models.Wiki(
        Title = title,
        Title_Count= count
    )
    print(count)
    main.create_Wiki(Wiki=Wiki_page, db=db)
    
