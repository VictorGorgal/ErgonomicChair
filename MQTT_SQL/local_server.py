import paho.mqtt.client as paho
import sqlite3
from os.path import exists
from multiprocessing import Process


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

        self.close()


class MQTT:
    def __init__(self, topic, username, password, broker, port=1883, client_id='cadeira1'):
        self.BROKER = broker
        self.PORT = port
        self.ID = client_id

        self.topic = topic
        self.username = username
        self.password = password

        self.client = paho.Client(client_id=self.ID, userdata=None, protocol=paho.MQTTv311)
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(self.BROKER, self.PORT)
        self.client.on_message = self.on_message
        self.client.subscribe(self.topic, qos=1)

        self.sql = SQL('data.db')

    def on_message(self, _, __, msg):
        payload = msg.payload.decode('ascii')
        print(f'Topic:{msg.topic}\nPayload:{payload}')

        self.sql.save(payload)


class Interface:
    def __init__(self):
        self.sql = SQL('data.db')

        p1 = Process(target=start)  # starts MQTT on another process
        p1.start()

    def get_daily(self):
        daily = []
        cursor = self.sql.open()
        for row in cursor.execute('select * from daily'):
            daily.append(row)
        self.sql.close()
        return daily

    def get_lifetime(self):
        lifetime = []
        cursor = self.sql.open()
        for row in cursor.execute('select * from lifetime'):
            lifetime.append(row)
        self.sql.close()
        return lifetime

    def get_percentage(self):
        cursor = self.sql.open()

        ok = 0
        not_ok = 0

        for row in cursor.execute('select * from daily'):
            date, _, *sensors = row
            # convert list of strings into list of booleans
            sensors = [True if x == '1' else False for x in sensors]
            if all(sensors):
                ok += 1
            else:
                not_ok += 1

        percentage = round(ok * 100 / (ok + not_ok), 2)

        self.sql.close()

        return percentage


def start():
    server = MQTT(topic='cadeira/1',
                  username='victor',
                  password='morenamorenas',
                  broker='192.168.10.6')

    print('Starting server...')
    server.client.loop_forever()


if __name__ == '__main__':
    interface = Interface()
    while True:
        t = input('insert: ')
        if t == 'd':
            print(interface.get_daily())
        elif t == 'l':
            print(interface.get_lifetime())
        elif t == 'p':
            print(interface.get_percentage())
        else:
            print('no')
