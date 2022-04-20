import time
import redis

class Rds():
    def __init__(self):
        self.rds = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
        self.msg = "Initializing"
        self.init()

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
        print("Main block running..")

    def write(self, key, data):
        self.rds.set(key, data)

    def read(self, key):
        return self.rds.get(key)

if __name__ == '__main__':
    data = Rds()
    data.run()