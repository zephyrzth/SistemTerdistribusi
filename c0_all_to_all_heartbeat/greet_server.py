from c0_all_to_all_heartbeat.greet import *
import Pyro4
import time
import threading


def start_without_ns():
    daemon = Pyro4.Daemon()
    x_GreetServer = Pyro4.expose(GreetServer)
    uri = daemon.register(x_GreetServer)
    print("my URI : ", uri)
    daemon.requestLoop()


class AllHeartbeat(GreetServer):
    def __init__(self):
        super().__init__()
        self.connect_to = ["greetserver2", "greetserver3"]
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
        ns.register("greetserver", uri_greetserver)
        daemon.requestLoop()

    def run(self):
        t1 = threading.Thread(target=self.start_with_ns)
        t2 = threading.Thread(target=self.coba_heartbeat)
        t1.start()
        t2.start()


if __name__ == '__main__':
    test = AllHeartbeat()
    test.run()
