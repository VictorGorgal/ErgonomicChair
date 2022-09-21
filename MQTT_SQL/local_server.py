import paho.mqtt.client as paho
import sqlite3
from os.path import exists
from json import loads
from datetime import datetime

import serial


class SQL:
    def __init__(self, file):
        self.file = file

        self.initDB()

    def open(self):
        self.connection = sqlite3.connect(self.file)
        return self.connection.cursor()

    def close(self):
        self.connection.close()

    def save(self, payload):
        cursor = self.open()

        self.check_date(payload, cursor)
        cursor.execute('insert into daily values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', payload.split(';'))

        self.connection.commit()
        self.close()

    def check_date(self, payload, cursor):
        payload_date = payload.split(';')[0]

        row = cursor.execute('select * from daily limit 1')
        try:
            first_row = row.fetchall()[0]
        except IndexError:
            return
        db_date = first_row[0]

        if payload_date == db_date:  # everything's ok
            return

        self.next_day(cursor)

    def clear(self, table, cursor):
        cursor.execute(f'delete from {table}')
        self.connection.commit()

    def next_day(self, cursor):
        ok = 0
        not_ok = 0
        date = ''

        for row in cursor.execute('select * from daily'):
            date, _, *sensors = row
            # convert list of strings into list of booleans
            sensors = [True if x == '1' else False for x in sensors]
            if all(sensors):
                ok += 1
            else:
                not_ok += 1

        percentage = round(ok * 100 / (ok + not_ok), 2)

        if date:
            cursor.execute(f'insert into lifetime values (?, ?)', [date, percentage])

        self.clear('daily', cursor)

    def save_real_time(self, payload):
        cursor = self.open()

        cursor.execute('UPDATE realTime SET measurement=(?) WHERE id=0', [payload])

        self.connection.commit()
        self.close()

    def initDB(self):
        if exists(self.file):
            return

        print('Creating database...')
        cursor = self.open()

        cursor.execute("""create table daily (
                        date text, 
                        time text, 
                        s1 blob, 
                        s2 blob, 
                        s3 blob, 
                        s4 blob, 
                        s5 blob, 
                        s6 blob, 
                        s7 blob, 
                        s8 blob)""")

        cursor.execute("""create table lifetime (
                        date text,
                        percentage real)""")

        cursor.execute("""create table realTime (measurement text)""")

        self.close()


class Serial:
    def __init__(self, com='COM3'):
        self.node = serial.Serial(com, 9600, timeout=5)

        self.sql = SQL('D:/Scripts/Python/Fetin/Fetin 2022/Cadeira/MQTT_SQL/data.db')

    def read_serial(self):
        while True:
            recieved = self.node.readline()
            self.on_message(recieved)

    def on_message(self, msg):
        if len(msg) > 150:
            return
        if msg == b'':
            return

        payload = msg.decode('ascii').strip()

        # print(f'Payload: {payload}')

        self.sql.save_real_time(payload)


def start():
    server = Serial(com='COM5')

    print('Starting server...')
    server.read_serial()


if __name__ == '__main__':
    start()
