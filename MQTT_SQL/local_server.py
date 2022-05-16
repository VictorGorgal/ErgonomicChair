import paho.mqtt.client as paho
import sqlite3
from os.path import exists


class MQTT_SQL:
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

    def on_message(self, _, __, msg):
        payload = msg.payload.decode('ascii')
        print(f'Topic:{msg.topic}\nPayload:{payload}')

        self.save(payload)

    @staticmethod
    def save(payload):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('insert into daily values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', payload.split(';'))

        connection.close()

    @staticmethod
    def initDB():
        if exists('./data.db'):
            return

        print('Creating database...')
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

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

        connection.close()


if __name__ == '__main__':
    server = MQTT_SQL(topic='cadeira/1',
                      username='victor',
                      password='morenamorenas',
                      broker='192.168.10.6')

    print('Starting server...')
    server.client.loop_forever()
