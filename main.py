import scrapper_functions as sf
from send_email import send_email
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"


class Database:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)

    def store(self, event):
        event = event.split(',')
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO events (band, city, date) VALUES (?,?,?)', event)
        self.connection.commit()

    def read(self, event):
        event = event.split(',')
        cursor = self.connection.cursor()
        cursor.execute('SELECT band, city, date FROM events WHERE band=? AND city=? AND date=?', event)
        result = cursor.fetchall()
        return result


if __name__ == "__main__":
    while True:
        source = sf.scrapper(URL)
        extracted = sf.extract(source)

        if extracted != "No upcoming tours":
            db = Database(database="data.db")
            if not db.read(extracted):
                db.store(extracted)
                # send_email(extracted)
