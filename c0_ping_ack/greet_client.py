import Pyro4
import time
from threading import Thread


class PingService(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server_status = False
        self.server = server

    def ping_check(self):
        counter = 0
        while True:
            if counter == 2:
                break
            try:
                if self.server.ping():
                    self.server_status = True
                    # print(self.server_status)
                else:
                    self.server_status = False
                    counter = counter + 1
            except:
                self.server_status = False
                counter = counter + 1
            time.sleep(2)

    def test_with_ns(self):
        counter = 0
        while True:
            time.sleep(2)
            if counter == 2:
                print('Server Failed')
                break
            if self.server_status:
                #actionType = input("Enter the input (0 - 4), -1 to exit : ")
                actionType = input("0 = Create File\n1 = Read File\n2 = Update File\n3 = Delete File\n4 = List files\nEnter the action type : ")
                if actionType == "0":
                    filename = input("Enter filename : ")
                    print(self.server.create_file(filename))
                elif actionType == "1":
                    filename = input("Enter filename : ")
                    print(self.server.read_file(filename))
                elif actionType == "2":
                    filename = input("Enter filename (textfile) : ")
                    contents = input("Enter text to write : ")
                    print(self.server.update_file(contents, filename))
                elif actionType == "3":
                    filename = input("Enter filename : ")
                    print(self.server.delete_file(filename))
                elif actionType == "4":
                    directory = input("Enter the directory to list : ")
                    hasil = self.server.list_file(directory)
                    for f in hasil:
                        print(f)
                else:
                    print("Wrong input!")
                print("\n")
            else:
                counter = counter + 1
                print("Can't connect to server\n")

    def run(self) -> None:
        t1 = Thread(target=self.ping_check)
        t2 = Thread(target=self.test_with_ns)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


def test_no_ns():
    uri = "PYRO:obj_27d7c59497c44c688319f7d8a4a95935@localhost:40549"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))


def test_with_ns():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))
    while (True):
        #actionType = input("Enter the input (0 - 4), -1 to exit : ")
        actionType = input("0 = Create File\n1 = Read File\n2 = Update File\n3 = Delete File\n4 = List files\n-1 = Exit the program\nEnter the action type : ")
        if actionType == "0":
            filename = input("Enter filename : ")
            print(gserver.create_file(filename))
        elif actionType == "1":
            filename = input("Enter filename : ")
            print(gserver.read_file(filename))
        elif actionType == "2":
            filename = input("Enter filename (textfile) : ")
            contents = input("Enter text to write : ")
            print(gserver.update_file(contents, filename))
        elif actionType == "3":
            filename = input("Enter filename : ")
            print(gserver.delete_file(filename))
        elif actionType == "4":
            directory = input("Enter the directory to list : ")
            hasil = gserver.list_file(directory)
            for f in hasil:
                print(f)
        elif actionType == "-1":
            break
        else:
            print("Wrong input!")
        print("\n")


if __name__ == '__main__':
    # filename = "D:\\Sistem_Terdistribusi\\sister2019\\c0"
    # contents = "Coba McQueen YaQueen"
    # 0 = Create, 1 = Read, 2 = Update, 3 = Delete, 4 = List all files
    # actionType = 4
    # test_with_ns()
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))
    pingAck = PingService(gserver)
    pingAck.run()
