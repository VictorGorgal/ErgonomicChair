from local_server import SQL, start
from multiprocessing import Process


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
