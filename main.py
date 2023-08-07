import requests

URL = "http://programmer100.pythonanywhere.com/tours/"

def scrapper(url):
    response = requests.get(url)
    source = response.text

    return source


if __name__ == "__main__":
    print(scrapper(URL))