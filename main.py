import time
import redis

class Rds():
    def __init__(self):
        self.rds = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
        self.msg = "Initializing"
        self.init()
        self.schedule = dict()

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
        for i in range(9):
            self.schedule[i] = start + i*5
        counter = 0
        while 1:
            if (int(time.time()) - start) % 10 == 0:
                print("{} - {}".format(counter, int(time.time())))
                time.sleep(1)
                counter += 1
                if counter == 9:
                    break

    def write(self, key, data):
        self.rds.set(key, data)

    def read(self, key):
        return self.rds.get(key)

if __name__ == '__main__':
    data = Rds()
    data.run()