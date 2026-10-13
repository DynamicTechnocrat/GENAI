import requests


def book_order() -> str:
    url = "http://127.0.0.1:5000/book"
    app = requests.get(url)
    return app.text