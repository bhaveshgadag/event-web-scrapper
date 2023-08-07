import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrapper(url):
    response = requests.get(url)
    source = response.text

    return source


def extract(data):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted = extractor.extract(data)["tours"]
    return extracted


if __name__ == "__main__":
    source = scrapper(URL)
    extracted = extract(source)
    print(extracted)