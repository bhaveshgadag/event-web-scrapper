import scrapper_functions as sf
from send_email import send_email
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")

def store(event):
    event = event.split(',')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO events (band, city, date) VALUES (?,?,?)', event)
    connection.commit()


def read(event):
    event = event.split(',')
    cursor = connection.cursor()
    cursor.execute('SELECT band, city, date FROM events WHERE band=? ' \
            'AND city=? AND date=?', event)
    result = cursor.fetchall()
    return result

if __name__ == "__main__":
    while True:
        source = sf.scrapper(URL)
        extracted = sf.extract(source)

        if extracted != "No upcoming tours":
            if not read(extracted):
                store(extracted)
                send_email(extracted)

    connection.close()
