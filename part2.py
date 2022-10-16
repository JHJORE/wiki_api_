


import requests


def make_treeview():
    values = 3
    URL = "http://127.0.0.1:8000/wiki/" + str(values)
    PARAMS = {"wikiid": values}

    response = requests.get(url = URL, params = PARAMS)
    aids = response.json()
    print(aids)

make_treeview()
