try:
    from .local_server import SQL, start
except:
    from local_server import SQL, start

from multiprocessing import Process


class Interface:
    NOT_SITTING = 0
    GOOD = 1
    BAD = 2

    def __init__(self):
        self.sql = SQL('D:/Scripts/Python/Fetin/Fetin 2022/Cadeira/MQTT_SQL/data.db')

        p1 = Process(target=start)  # starts MQTT on another process
        p1.daemon = True  # closes thread when program finishes
        p1.start()

    def get_real_time(self):
        cursor = self.sql.open()
        measurement = list(cursor.execute('select * from realTime'))[0][1]
        self.sql.close()
        return measurement

    def get_daily(self):
        daily = []
        cursor = self.sql.open()
        for row in cursor.execute('select * from daily'):
            daily.append(row)
        self.sql.close()
        return daily

    # Gets the daily information as a list to build the home progress bar
    def get_daily_list(self):
        daily = self.get_daily()
        minutes = 0  # Absolute time from measurement
        total_time = 0  # Total time on a certaing position
        last_minutes = 0  # Time since last measurement
        state = Interface.NOT_SITTING  # User state
        last_state = state  # Last user state
        bars = []  # List to return

        for measure in daily:
            hours = measure[1]
            hour, minute, _ = hours.split(':')
            minutes = int(hour) * 60 + int(minute)  # Absolute time
            delta = minutes - last_minutes  # Time since last measurement

            # If the time since the last measurement exceeds 5 minutes, because user is not sitting on chair
            if delta > 5:
                state = Interface.NOT_SITTING
            else:
                state = self.get_user_state_from_measurement(measure)

            if state != last_state:
                bars.append((last_state, total_time))
                last_state = state
                total_time = 0

            total_time += delta
            last_minutes = minutes

        bars.append((state, total_time))  # Append last iteration
        if minutes < 1440:
            bars.append((Interface.NOT_SITTING, 1440 - minutes))

        return bars

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

        if ok + not_ok == 0:
            percentage = 0
        else:
            percentage = round(ok * 100 / (ok + not_ok), 2)

        self.sql.close()

        return percentage

    @staticmethod
    def get_user_state_from_measurement(m):
        date, _, *sensors = m
        # convert list of strings into list of booleans
        sensors = [True if x == '1' else False for x in sensors]

        if all(sensors):
            return Interface.GOOD
        elif any(sensors):
            return Interface.BAD
        else:
            return Interface.NOT_SITTING


if __name__ == '__main__':
    interface = Interface()
    while True:
        t = input('insert: ')
        if t == 'r':
            print(interface.get_real_time())
        elif t == 'd':
            print(interface.get_daily())
        elif t == 'dl':
            print(interface.get_daily_list())
        elif t == 'l':
            print(interface.get_lifetime())
        elif t == 'p':
            print(interface.get_percentage())
        else:
            print('no')
