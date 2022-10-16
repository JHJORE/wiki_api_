import json
import requests
from bs4 import BeautifulSoup
import models, main
from database import SessionLocal

db = SessionLocal()


def wiki_repseonse():
    response_API = requests.get("https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=Vipps")
    package_response = json.loads(response_API.text).get("parse")

    title = package_response.get("title")
    text = package_response.get("text").get("*")
    soup = BeautifulSoup(text, "html.parser")

    count = 0
    for page in soup.findAll('p'):
        count += page.getText().count(title)
    
    Wiki_page = models.Wiki(
        Title = title,
        Title_count = count
    )

    main.create_Wiki(Wiki=Wiki_page, db= db)
    
    print(count)

