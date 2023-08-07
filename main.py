import scrapper_functions as sf

URL = "http://programmer100.pythonanywhere.com/tours/"


def store(event):
    with open("events.txt", "a") as file:
        return file.write(event + "\n")


def read():
    with open("events.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    source = sf.scrapper(URL)
    extracted = sf.extract(source)

    if extracted != "No upcoming tours":
        if extracted not in read():
            store(extracted)

    print(extracted)
