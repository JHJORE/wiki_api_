import json
import requests
from bs4 import BeautifulSoup
from sql_app.database import SessionLocal
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
    
    
    
    print(count)

