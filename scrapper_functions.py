import requests
import selectorlib


def scrapper(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(data):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted = extractor.extract(data)["tours"]
    return extracted
