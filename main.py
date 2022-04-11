import time
import redis

class Rds():
    def __init__(self):
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

if __name__ == '__main__':
    data = Rds()
    data.run()