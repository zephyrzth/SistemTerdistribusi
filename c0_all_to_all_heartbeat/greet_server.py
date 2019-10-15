from c0_all_to_all_heartbeat.greet import *
import Pyro4
import time
import threading

class AllHeartbeat(GreetServer):
    def __init__(self):
        super().__init__()

def start_without_ns():
    daemon = Pyro4.Daemon()
    x_GreetServer = Pyro4.expose(GreetServer)
    uri = daemon.register(x_GreetServer)
    print("my URI : ", uri)
    daemon.requestLoop()


class AllHeartbeat(GreetServer):
    def __init__(self):
        super().__init__()
        self.connect_to = ["greetserver2"]
        self.gserver = []
        self.client_id = []
        self.t = []

    def coba_heartbeat(self):
        i = 0
        for x in self.connect_to:
            uri = "PYRONAME:{}@localhost:7777".format(x)
            self.gserver[i] = Pyro4.Proxy(uri)
            self.client_id[i] = self.gserver[i].get_device_total()
            print(self.gserver[i].add_device(self.client_id[i]))
            i = i + 1
            self.t[i] = threading.Thread(target=self.send_heartbeat, args=(self.gserver[i], self.client_id[i]))
            self.t[i].start()

    def send_heartbeat(self, gserver, client_id):
        while True:
            time.sleep(5)
            print(gserver.add_heartbeat(client_id))
            gserver.central_heartbeat()

    def start_with_ns(self):
        # name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
        # gunakan URI untuk referensi name server yang akan digunakan
        # untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list
        daemon = Pyro4.Daemon(host="localhost")
        ns = Pyro4.locateNS("localhost", 7777)
        x_GreetServer = Pyro4.expose(GreetServer)
        uri_greetserver = daemon.register(x_GreetServer)
        print("URI greet server : ", uri_greetserver)
        ns.register("greetserver2", uri_greetserver)
        daemon.requestLoop()

    def run(self):
        t1 = threading.Thread(target=self.start_with_ns)
        t2 = threading.Thread(target=self.coba_heartbeat)
        t1.start()
        t2.start()


if __name__ == '__main__':
    test = AllHeartbeat()
    test.run()
