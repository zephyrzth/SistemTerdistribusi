import random
import os
import glob

class GreetServer(object):
    def __init__(self):
        pass

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

    def ping(self):
        return True

if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('Dhana'))
