import requests

def get_wiki(value):
    URL = "http://127.0.0.1:8000/wiki/titles/" + str(value)
    PARAMS = {"WikiTitle": value}
    response = requests.get(url = URL, params = PARAMS)
    info = response.json()
    print(info)


