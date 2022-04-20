import time
import redis

class Rds():
    def __init__(self):
        self.rds = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
        self.msg = "Initializing"
        self.init()
        self.schedule = dict()
        self.charging_time = 60
        self.number_of_relays = 9

    def run(self):
        while(1):
            try:
                self.main()
                time.sleep(1)
            except Exception as e:
                print(e)

    def init(self):
        print(self.msg)

    def main(self):
        start = int(time.time())
        print("Initial time: {}".format(time.time()))
        counter = 0
        while 1:
            if (int(time.time()) - start) % self.charging_time == 0:
                print("{} - {}".format(counter, int(time.time())))
                time.sleep(1)
                counter += 1
                if counter == self.number_of_relays:
                    break

    def write(self, key, data):
        self.rds.set(key, data)

    def read(self, key):
        return self.rds.get(key)

if __name__ == '__main__':
    data = Rds()
    data.run()