import Pyro4


def get_fileserver_object():
    uri = "PYRONAME:fileserver@localhost:7777"
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    #print(f.create('coba.txt'))
    print(f.list())
    #print(f.read('coba.txt'))
    #print(f.delete('f2'))

