import json
import requests
from bs4 import BeautifulSoup
import database 
import models, main




def wiki_repseonse(topic):

    db = database.SessionLocal()
    URL = f"https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={topic}"
    response_API = requests.get(URL)
    package_response = json.loads(response_API.text).get("parse")

    if package_response is None:
        return print("cant find package")

    title = package_response.get("title")
    text = package_response.get("text").get("*")
    soup = BeautifulSoup(text, "html.parser")

    print(title)

    count = 0
    for page in soup.findAll('p'):
        count += page.getText().count(title)
    print(count)

    Wiki = models.Wiki(
        Title = title,
        Title_Count= count
    )
    
    main.create_Wiki(Wiki=Wiki, db=db)
    