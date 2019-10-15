import random
import os
import glob
import time
import threading

CHECK_TIMEOUT = 15

class GreetServer(object):
    def __init__(self):
        self.connected_device = {}
        self.failed_device = []

    def get_device_total(self):
        return len(self.connected_device)

    def add_device(self, device_id):
        self.connected_device[device_id] = time.time()
        print("Device {} added\n".format(device_id))
        return "Successfully added\n"

    def add_heartbeat(self, device_id):
        self.connected_device.update({
            device_id : time.time()
        })
        print("Device {} heartbeat received\n".format(device_id))
        return "Heartbeat success\n"

    def check_heartbeat(self):
        while True:
            limit = time.time() - CHECK_TIMEOUT
            self.failed_device = [device_id for (device_id, lastTime) in self.connected_device.items() if lastTime < limit]
            for x in self.failed_device:
                self.connected_device.pop(x)
                print("Device {} failed\n".format(x))
            self.failed_device = []

    def central_heartbeat(self):
        t1 = threading.Thread(target=self.check_heartbeat)
        t1.start()

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def create_file(self, name):
        f = open(name, "w+")
        f.close()
        return "File " + name + " Created!"

    def read_file(self, name):
        f = open(name, "r")
        if f.mode == 'r':
            contents = f.read()
        f.close()
        return contents

    def update_file(self, newContents, name):
        f = open(name, "r")
        contents = f.read()
        f.close()

        f = open(name, "w")
        f.write(newContents)
        f.close()
        return "File " + name + " Updated!"

    def delete_file(self, name):
        os.remove(name)
        return "File " + name + " Removed!"

    def list_file(self, directory):
        hasil = []
        files = [f for f in glob.glob(directory + "**/*", recursive=True)]
        for f in files:
            hasil.append(f)
        return hasil

if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('Dhana'))
