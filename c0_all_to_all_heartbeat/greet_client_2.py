from c0_all_to_all_heartbeat.greet import *
import Pyro4
import time
import threading


class AllHeartbeat(GreetServer):
    def __init__(self):
        super().__init__()
        self.connect_to = ["greetserver", "greetserver2"]
        self.gserver = []
        self.client_id = []
        self.t = []

    def coba_heartbeat(self):
        for x in self.connect_to:
            flag = False
            uri = "PYRONAME:{}@localhost:7777".format(x)
            while flag == False:
                time.sleep(5)
                try:
                    self.gserver.append(Pyro4.Proxy(uri))
                    device_id = self.gserver.index(Pyro4.Proxy(uri))
                    #print(device_id)
                    self.client_id.append(device_id)
                    print(self.gserver[device_id].add_device(device_id, x))
                    self.t.append(threading.Thread(target=self.send_heartbeat, args=(device_id, x,)))
                    self.t[device_id].start()
                    flag = True
                except:
                    print("Device {} not running!\n".format(x))

    def send_heartbeat(self, device_id, device_name):
        while True:
            time.sleep(5)
            try:
                print(self.gserver[device_id].add_heartbeat(device_id, device_name))
                self.gserver[device_id].central_heartbeat()
            except:
                continue

    def start_with_ns(self):
        # name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
        # gunakan URI untuk referensi name server yang akan digunakan
        # untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list
        daemon = Pyro4.Daemon(host="localhost")
        ns = Pyro4.locateNS("localhost", 7777)
        x_GreetServer = Pyro4.expose(GreetServer)
        uri_greetserver = daemon.register(x_GreetServer)
        print("URI greet server : ", uri_greetserver)
        ns.register("greetserver3", uri_greetserver)
        daemon.requestLoop()

    def run(self):
        t1 = threading.Thread(target=self.start_with_ns)
        t2 = threading.Thread(target=self.coba_heartbeat)
        t1.start()
        t2.start()


def test_no_ns():
    uri = "PYRO:obj_27d7c59497c44c688319f7d8a4a95935@localhost:40549"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))


def test_with_ns():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))
    while (True):
        actionType = input(
            "0 = Create File\n1 = Read File\n2 = Update File\n3 = Delete File\n4 = List files\n-1 = Exit the program\nEnter the action type : ")
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
    test = AllHeartbeat()
    test.run()
